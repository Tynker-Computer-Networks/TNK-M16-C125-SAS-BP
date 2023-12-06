#!/usr/bin/env  python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if (file == "virus.py" or file == "encryptedKey.key" or file == "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)


# Create variable secretePhrase and store the value "hello" or any other


# Ask user to enter the valid phrase to decrypt the files


# Check if secretPhrase do not match with the enteredPhrase

    # Print " 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 "

# Else:

    # Add try block

        # Read the encryptedKey.key file and store the content in secretKey variable.



        # Iterate the loop over the files list

            # Open the file in rb mode and store the content in rawData variable

            # Use Fernet(secretKey).decrypt(rawData) to decrypt and store the result in decryptRawData variable


            # Update the same file with decrypted data


        # Notify the message to the user "You have successfully recovered all the files!!"

    # Except pass 

