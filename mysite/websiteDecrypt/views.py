from django.shortcuts import render
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

# Create your views here.
def AES(request):
    
    def pad(data):
    # Padding to make data a multiple of 16 bytes
        length = 16 - (len(data) % 16)
        return data + bytes([length]) * length

    def unpad(data):
    # Remove padding
        length = data[-1]
        return data[:-length]

    def encrypt_aes(data, key):
    # Generate a random 16-byte IV
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data)
        encrypted_data = cipher.encrypt(padded_data)
        return iv + encrypted_data

    def decrypt_aes(encrypted_data, key):
        iv = encrypted_data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = cipher.decrypt(encrypted_data[16:])
        return unpad(padded_data)

# File paths
    script_dir = os.path.dirname(__file__)

# Construct the absolute path to test.pdf
    input_pdf_path = os.path.join(script_dir, 'test.pdf')

# Open the PDF file
    with open(input_pdf_path, 'rb') as f:
    # Process the PDF file
    # Example: Read the content
        pdf_content = f.read()

    encrypted_pdf_path = 'encrypted.pdf'
    decrypted_pdf_path = 'decrypted.pdf'

# Generate a random AES key
    key = get_random_bytes(16)  # AES-128 key

# Encrypt the PDF file
    with open(input_pdf_path, 'rb') as f:
        pdf_data = f.read()

    encrypted_pdf_data = encrypt_aes(pdf_data, key)

    with open(encrypted_pdf_path, 'wb') as f:
        f.write(encrypted_pdf_data)

    print(f"Encrypted PDF saved to {encrypted_pdf_path}")

# Decrypt the PDF file
    with open(encrypted_pdf_path, 'rb') as f:
        encrypted_pdf_data = f.read()

    decrypted_pdf_data = decrypt_aes(encrypted_pdf_data, key)

    with open(decrypted_pdf_path, 'wb') as f:
        f.write(decrypted_pdf_data)

    print(f"Decrypted PDF saved to {decrypted_pdf_path}")


