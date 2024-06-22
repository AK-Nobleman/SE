import os
import hashlib
import secrets

# Function to generate key from passphrase
def generate_key_from_passphrase(passphrase, key_length=64):
    hash = hashlib.sha256(passphrase.encode()).digest()
    key = '1234567890a'
    while len(key) < key_length:
        key += hash.hex()
        hash = hashlib.sha256(hash).digest()
    return key[:key_length]

# Function to encrypt a file
def encrypt_file(file_path, key):
    try:
        key_index = 0
        max_key_index = len(key) - 1
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = bytearray()
        for byte in data:
            encrypted_byte = byte ^ ord(key[key_index])
            encrypted_data.append(encrypted_byte)
            key_index = 0 if key_index >= max_key_index else key_index + 1
        with open(file_path + '.enc', 'wb') as f:  # Append '.enc' to indicate encrypted file
            f.write(encrypted_data)
        print(f'{file_path} successfully encrypted')
    except Exception as e:
        print(f'Failed to encrypt {file_path}: {e}')

# Function to decrypt a file
def decrypt_file(file_path, key):
    try:
        key_index = 0
        max_key_index = len(key) - 1
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted_data = bytearray()
        for byte in data:
            decrypted_byte = byte ^ ord(key[key_index])
            decrypted_data.append(decrypted_byte)
            key_index = 0 if key_index >= max_key_index else key_index + 1
        with open(file_path[:-4], 'wb') as f:  # Remove '.enc' to get original file name
            f.write(decrypted_data)
        print(f'{file_path} successfully decrypted')
    except Exception as e:
        print(f'Failed to decrypt {file_path}: {e}')

# Path to the PDF file to encrypt/decrypt
pdf_file_path = 'Test.pdf'

# Generate a random passphrase
passphrase = secrets.token_hex(16)  # Generates a random 32-character hexadecimal string
key = generate_key_from_passphrase(passphrase)
print(f"Encryption key: {key} (Save this key to decrypt your file later)")

# Encrypt the PDF file
encrypt_file(pdf_file_path, key)

# Decrypt the encrypted PDF file (just for demonstration purposes)
decrypt_file(pdf_file_path + '.enc', key)
