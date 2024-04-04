import re

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
key = ""
correct = False


def encry(message,key):
  message = list(re.sub("[^A-Z]", "", message, count=0, flags=re.IGNORECASE).lower())
  encryp = ""
  for i in message:
    encryp += key[alphabet.index(i)]
  return encryp
  
def decry(message,key):
  message = list(re.sub("[^A-Z]", "", message, count=0, flags=re.IGNORECASE).lower())
  decryp = ""
  for i in message:
    decryp += alphabet[key.index(i)]
  return decryp
      

while not correct:
  key = input("Enter your key in the form of a series of every letter in the "
    "alphabet, each used once.\nEx: 'zxdf...' : ").lower()
  print(key)
  if key.isalpha():
    key = list(key)
    if len(key) == 26 and len(key) == len(set(key)):
      correct = True
      print("Valid key inputted.")
    else:
      print("Invalid key. Please try again.")
  else:
    print("Error: Only enter letters.")
correct = False

while not correct:
  userinp = input("[1] Encrypt a message\n[2] Decrypt a message\n")
  if userinp == '1':
    correct = True
    message = input("Please enter the message you would like to encrypt: ")
    print("Encrypted message:\n", encry(message, key))
  elif userinp == '2':
    correct = True
    message = input("Please enter the message you would like to decrypt: ")
    print("Decrypted message:\n", decry(message, key))
  else:
    print("Error: Invalid input.")

exit(0)