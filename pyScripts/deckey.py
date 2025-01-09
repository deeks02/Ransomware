import os
from cryptography.fernet import Fernet

def ransomware_decrypt():
    exclude_files = ["script.py", "thekey.key", "deckey.py", "script", "deckey"]
    
    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    for file in os.listdir():
        if file in exclude_files:
            continue
        if os.path.isfile(file):
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)

    print("There you go!! All your files are decrypted")

if __name__ == "__main__":
    ransomware_decrypt()