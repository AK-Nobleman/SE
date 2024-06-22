import os
import glob
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to generate a random AES encryption key
def generate_aes_key(key_size):
    return get_random_bytes(key_size // 8)

def encrypt_file(key, file_path):
    buffer_size = 64 * 1024  # 64 KB buffer size
    encrypted_file = file_path + '.aes'

    # Encrypt the file
    with open(file_path, 'rb') as f_plain:
        with open(encrypted_file, 'wb') as f_encrypted:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(f_plain.read())
            [f_encrypted.write(x) for x in (cipher.nonce, tag, ciphertext)]

    # Remove the plain file after encryption
    

    # Optionally, return the path to the encrypted file
    return encrypted_file

def decrypt_file(key, encrypted_file):
    buffer_size = 64 * 1024  # 64 KB buffer size
    decrypted_file = encrypted_file[:-4]  # Remove '.aes' extension to get original file name

    # Decrypt the file
    with open(encrypted_file, 'rb') as f_encrypted:
        nonce, tag, ciphertext = [f_encrypted.read(x) for x in (16, 16, -1)]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        f_decrypted = open(decrypted_file, 'wb')
        f_decrypted.write(cipher.decrypt_and_verify(ciphertext, tag))

    # Remove the encrypted file after decryption
    

    # Optionally, return the path to the decrypted file
    return decrypted_file

def encrypt_files_in_directory(directory):
    # List all plain files in the directory
    plain_files = glob.glob(os.path.join(directory, '*'))
    

    # Generate a random AES key
    key_size = 256  # AES-256
    key = generate_aes_key(key_size)
    
    for file_path in plain_files:
        try:
            encrypted_file = encrypt_file(key, file_path)
            print(f'{file_path} successfully encrypted to {encrypted_file}')
        except Exception as e:
            print(f'Failed to encrypt {file_path}: {e}')

def decrypt_files_in_directory(directory):
    # List all encrypted files in the directory
    encrypted_files = glob.glob(os.path.join(directory, '*.aes'))

    # Prompt for the AES key (in a real scenario, securely manage and retrieve the key)
    key_size = 256  # AES-256
    key = generate_aes_key(key_size)

    for encrypted_file in encrypted_files:
        try:
            decrypted_file = decrypt_file(key, encrypted_file)
            print(f'{encrypted_file} successfully decrypted to {decrypted_file}')
        except Exception as e:
            print(f'Failed to decrypt {encrypted_file}: {e}')

if __name__ == "__main__":
    directory = r'Test.pdf'  # Replace with your directory containing files
    
    # Encrypt files in the directory
    encrypt_files_in_directory(directory)
    print(directory)
    # Decrypt encrypted files in the directory
    decrypt_files_in_directory(directory)
