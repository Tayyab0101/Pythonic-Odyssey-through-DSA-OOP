#Caesar Cypher!!!!!!!!
from string import *

def encode(msg, shift):
    encoded_msg = ""
    for char in msg:
        if char in ascii_lowercase:
            index = (ascii_lowercase.index(char) + shift) % 26
            encoded_msg += ascii_lowercase[index]
        elif char in ascii_uppercase:
            index = (ascii_uppercase.index(char) + shift) % 26
            encoded_msg += ascii_uppercase[index]
        else:
            encoded_msg += char  # for example spaces or special chars
    return encoded_msg

def decode(msg, shift):
    return encode(msg, -shift)

msg = input("Enter your message: ")
op = input("Enter the type of operation (Encode or Decode): ").lower()
shift = int(input("How many positions do you want to shift? "))

if op == "encode":
    encoded_message = encode(msg, shift)
    print("Encoded message:", encoded_message)
elif op == "decode":
    decoded_message = decode(msg, shift)
    print("Decoded message:", decoded_message)
else:
    print("Invalid operation. Please choose 'encode' or 'decode'.")
