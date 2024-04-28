# decimal to octal
print('oct(10) is:', oct(10))

# binary to octal
print('oct(0b101) is:', oct(0b101))

# hexadecimal to octal
print('oct(0XA) is:', oct(0XA))

number = 15

# convert 15 to its binary equivalent 
print('The binary equivalent of 15 is', bin(number))

# Output: The binary equivalent of 15 is 0b1111

number = 5 

# convert 5 to its binary equivalent
print('The binary equivalent of 5 is:', bin(number))

number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print('Return type from hex() is', returnType)
