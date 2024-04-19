import random

ran = False
alphabet = list('abcdefghijklmnopqrstuvwxyz')

def rand_key(message):
    message = list(message)
    key = ""
    for i in message:
        key = key + chr(random.randint(0,200))
    return key
def encrypt(message, key):
    encry_mess =""
    counter = 0
    for i in message:
        encry_mess = encry_mess + chr(ord(i) ^ ord(key[counter]))
    return encry_mess

while not ran:
    with open('input.txt', 'r') as f:
        message = f.read()
    print("Inputted message: \n",message)
    user_choice = input("This program can encrypt and decrypt messages using One-Time Pad. Enter '1' for encryption and '2' for decryption: ")
    if user_choice == '1':
        key = rand_key(message)
        ciphertxt = encrypt(message, key)
        print("Encrypted message: \n", ciphertxt)
        print("Encryption key: \n", key)
        ran = True
    elif user_choice == '2':
        key = input("Enter the encryption key: ")
        #add if statement for if the key isnt formatted correctly
        message = encrypt(message, key)
        print("Decrypted message: \n", message)
        ran = True
    else:
        print("Invalid choice. Please enter '1' or '2'.")
    