# btyes and byte array
byte1 = bytes([65, 66, 97])
byte2 = bytearray([65, 66, 97])  # It is mutable
print(byte1,byte2) # or print(byte1.decode('ascii'), byte2.decode('ascii'))

# conversions of data type
print(oct(2))
print(hex(2))
x = bin(2) # int to bin
print(x[2:])
result = int(str(100), 2) # bin to int
print(result)
print(ord("B")) # Unicode
print(chr(65))

# Escae charcter
print('I\'llcal'l you later') # Backslash
print("Hello\tworld!") # Tab space
print("no__benefits__of_studying\rHuge_benefits_") #Carriage return
