# Bases.py
##Summary
*This module is for running calculations
and conversions on integers in a variety of bases.*

##Examples
###To convert a decimal number, 12, to binary:
```python
bNum = decToBin(12)
```

###To convert a binary number, 00010110, to decimal:
```python
dNum = binToDec("00010110")
```

###To convert a decimal number, 42, to hexadecimal:
```python
hNum = decToHex(35) 
```

##Signed Integer Support
*Signed integers are currently supported in
converting between number bases, but are
considered unstable. There is not a function
for converting signed hexadecimal to signed binary
currently, but the functionality is possible
through separate conversions.*

##More Examples
###To convert the signed decimal number, -5, to binary:
```python
bNum = decToBin(-5)
```

###To convert the signed binary integer, 11111001, to decimal:
```python
dNum = binToDec("11111001", signed=True)
```

###To convert the signed decimal number, -24, to hexadecimal:
```python
hNum = decToHex(-24)
```

###To convert the signed hexadecimal, E8, to decimal:
```python
dNum = hexToDec("E8", signed=True)
```
