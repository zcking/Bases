"""
File: bases.py
Author: Zachary King
Description: This module is for running calculations
and conversions on integers in a variety of bases.

Examples:
(to convert a decimal number, 12, to binary)
bNum = decToBin(12) ----> returns "00001100"

(to convert a binary number, 00010110, to decimal)
dNum = binToDec("00010110") ----> returns 22

(to convert a decimal number, 42, to hexadecimal)
hNum = decToHex(35) ----> returns "2A" 

---Unsigned Integer Support---
Unsigned integers are currently supported in
converting between number bases, but are
considered unstable. There is not a function
for converting signed hexadecimal to signed binary
currently, but the functionality is possible
through separate conversions.

(to convert the signed decimal number, -5, to binary)
bNum = decToBin(-5) ----> returns "11111011" # no difference than with +5

(to convert the signed binary integer, 11111001, to decimal)
dNum = binToDec("11111001", signed=True) ----> returns -7 # signed is False by default

(to convert the signed decimal number, -24, to hexadecimal)
hNum = decToHex(-24) ----> returns "E8" # no difference than with +24

(to convert the signed hexadecimal, E8, to decimal)
dNum = hexToDec("E8", signed=True) ----> returns -24 # signed is False by default
"""

hexLetters = "ABCDEF"

def decToBin(decNumber):
	"""Converts a decimal number to binary.
	Negative numbers are converted to signed binary."""
	if decNumber < 0: return __signedDecToBin(decNumber)
	b = bin(decNumber)[2:]
	r = len(b) % 8
	dNum = ""
	if r != 0:
		for i in range(8-r):
			dNum += "0"
	dNum += bin(decNumber)[2:]
	return dNum

def decToHex(decNumber):
	"""Converts a given decimal number to hexadecimal.
	Negative number are converted to signed hexadecimal."""
	if decNumber < 0: return __signedDecToHex(decNumber)
	try:
		hexString = ""
		while (decNumber > 0):
			decNumber, rem = divmod(decNumber, 16)
			rem = int(rem)
			if rem < 10:
				hexString += str(rem)
			else:
				rem -= 10
				hexString += hexLetters[rem]
		return hexString[::-1] # reverse the digits
	except:
		return ""

def binToDec(binaryString, signed=False):
	"""Converts a given binary string to decimal.
	If signed is True, binaryString is treated as signed."""
	try:
		if (binaryString[0] == "1" and signed): return __signedBinToDec(binaryString)
		ndigits = len(binaryString)
		total = 0
		currentDigit = ndigits
		for digit in binaryString:
			symbol = int(digit)
			total += (symbol * pow(2, currentDigit-1))
			currentDigit -= 1
		return(total)
	except:
		return(-1)

def binToHex(binaryString, signed=False):
	"""Returns the given binaryString converted to hexadecimal.
	If signed is True, binaryString is treated as signed."""
	try:
		if (len(binaryString) > 0 and binaryString[0] == "1" and signed):
			return __signedBinToHex(binaryString)
		dec = abs(binToDec(binaryString))
		return decToHex(dec)
	except:
		return ""

def hexToDec(hexString, signed=False):
	"""Converts a given hexadecimal string to decimal.
	If signed is True, hexString is treated as signed."""
	try:
		if (hexString[0] in hexLetters+"89" and signed): return __signedHexToDec(hexString)
		ndigits = len(hexString)
		total = 0
		currentDigit = ndigits
		for digit in hexString:
			symbol = None
			if digit in hexLetters:
				symbol = hexLetters.index(digit) + 10
			else:
				symbol = int(digit)
			total += (symbol * pow(16, currentDigit-1))
			currentDigit -= 1
		return total
	except: 
		return -1

def hexToBin(hexString):
	"""Returns the given hexadecimal string converted to binary.
	**No signed hexString support currently**"""
	if len(hexString) == 0: return ""
	dec = hexToDec(hexString)
	return decToBin(dec)

def decTwoComplement(decNumber):
	"""Returns the two's complement of a given decimal number."""
	return binToDec(binTwoComplement(decToBin(decNumber)))

def binTwoComplement(binaryString):
	"""Returns the two's complement of a given binary string."""
	if (binaryString == ""): return ""
	comp = ""
	# Flip the bits
	for digit in binaryString:
		if digit == "1": comp += "0"
		if digit == "0": comp += "1"
	dec = binToDec(comp) + 1 # Add 1 to it
	return (bin(dec)[2:]) # Return complement

def hexTwoComplement(hexString):
	"""Returns the two's complement of a given hexadecimal string."""
	return binToHex(binTwoComplement(hexToBin(hexString)))

def decTwoComplement(decNumber):
	"""Returns the two's complement of a given decimal number."""
	return binToDec(binTwoComplement(decToBin(decNumber)))

def __signedDecToBin(decNumber):
	"""Converts a signed decimal number to binary. 
	*Note: not used by user."""
	return binTwoComplement(decToBin((abs(decNumber))))

def __signedDecToHex(decNumber):
	"""Converts a signed decimal number to hexadecimal. 
	*Note: not used by user."""
	return hexTwoComplement(decToHex(abs(decNumber)))

def __signedBinToDec(binaryString):
	"""Returns the given signed binaryString converted to a signed decimal integer.
	*Note: not used directly by user."""
	return binToDec(binTwoComplement(binaryString)) * -1

def __signedBinToHex(binaryString):
	"""Returns the given signed binaryString converted to a signed decimal integer.
	*Note: not used directly by user."""
	dec = __signedBinToDec(binaryString)
	return __signedDecToHex(dec)

def __signedHexToDec(hexString):
	"""Returns the given signed hexString converted to a signed decimal integer.
	*Note: not used directly by user."""
	return hexToDec(hexTwoComplement(hexString)) * -1
	
def addBinToBin(binaryStringOne, binaryStringTwo, signed=False):
	"""Returns the sum of the two given binary strings, in binary form.
	The signed argument represents BOTH binary strings.
	Note: use the alternative addBinToBin function for adding
	\tsigned and unsigned together."""
	one = binToDec(binaryStringOne, signed)
	two = binToDec(binaryStringTwo, signed)
	return decToBin(one + two)

def addBinToBin(binaryStringOne, binaryStringTwo, oneSigned=False, twoSigned=False):
	"""Returns the sum of the two given binary strings, in binary form.
	This version is for adding an unsigned and a signed integer."""
	one = binToDec(binaryStringOne, oneSigned)
	two = binToDec(binaryStringTwo, twoSigned)
	return decToBin(one + two)

# Tests below
# -----------
# print(addBinToBin("10111000", "00010000", False, True)) # should return "11001000" -> -56
# print(addBinToBin("10111000", "00010000", False)) # should return "11001000" -> 200
# print(binToDec("00001001")) # Test binToDec; should return 9
# print(decToHex(422)) # Test decToHex; should return "1A6"
# print(binTwoComplement("00000001")) # Test binTwoComplement; should return "11111111"
# print(hexToDec("1A6")) # Test hexToDec; should return 422
# print(hexTwoComplement("A9F")) # Test hexTwoComplement; should return "561"
# print(binToHex("00011110")) # Test binToHex; should return "1E"
# print(decToBin(14)) # Test decToBin; should return "1110"
# print(hexToBin("A9D2")) # Test hexToBin
# print(decTwoComplement(9)) # Test decTwoComplement; should return 7
