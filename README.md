# Ransomware Simulation Tool

This repository contains two Python scripts that simulate ransomware behaviour: one for encrypting files (`script.py`) and another for decrypting them (`deckey.py`). This project is designed strictly for educational purposes to demonstrate how ransomware operates. It uses Python, the `cryptography` library for encryption, PyInstaller for creating executable files, `exiftool` for steganography, and virtual machines (Linux and Windows) for demonstrating how the executable scripts can look like in different environments. The `chmod` command on Linux is also used to demonstrate how to provide executable permissions.

## Features

- Encrypts all files in the current directory (excluding specific files).
- Generates a unique encryption key.
- Decrypts files using the generated key.
- Demonstrates the structure and basic functionality of ransomware.
- Provides `.exe` files for use in Windows environments.
- Demonstrates steganography to hide content within images using `exiftool`.
- Disguises the script as an image file (e.g., `Dogpic.jpeg`).
- Updated logos for both Linux and Windows virtual machines.
- Includes a screenshot demonstrating the script running and decrypting files.
- Demonstrates the use of `chmod` to provide executable permissions on Linux.

## Files

1. `script.py`: The encryption script that encrypts files in the directory.
2. `deckey.py`: The decryption script that restores files to their original state.
3. `thekey.key`: The file that stores the encryption key generated during the encryption process.
4. `.exe` files: Executable versions of the scripts for Windows environments.
5. **Images**: Screenshots and demonstration images showcasing steganography, disguised scripts, and logo changes.

## How It Works

### Encryption (`script.py`)

- Generates a unique encryption key using `Fernet` from the `cryptography` library.
- Encrypts all files in the current directory except for specified excluded files.
- Saves the encryption key in a file named `thekey.key`.

### Decryption (`deckey.py`)

- Reads the encryption key from `thekey.key`.
- Decrypts all previously encrypted files.
- Restores files to their original state.

### Steganography and `.exe` Conversion

- The scripts have been converted into `.exe` files for use in Windows environments.
- Steganography techniques are demonstrated to hide sensitive content within images using `exiftool`.
- The script is disguised as an image file (e.g., `Dogpic.jpeg`) for demonstration purposes.
- Updated logos for demonstration in both Linux and Windows virtual machines.

### Screenshot Demonstration

- A screenshot is included that demonstrates the script running and decrypting files.

## Excluded Files

The following files are excluded from encryption and decryption:

- `script.py`
- `thekey.key`
- `deckey.py`
- `script`
- `deckey`
- Any `.exe` files

You can modify the `exclude_files` list in the scripts to customize exclusions.

## Disclaimer

This project is intended for educational and research purposes only. Use the scripts in a controlled and safe environment. Unauthorized use of these scripts in real-world scenarios is illegal and unethical. By using this tool, you agree to take full responsibility for any consequences that arise from its use.

> [!CAUTION]
> **DO NOT use this tool for malicious purposes.**
