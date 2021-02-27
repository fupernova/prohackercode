import binascii
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Run 'python3 aescbc_encrypt.py > ciphertext.json'

# Set up key, plaintext and iv
key = bytearray.fromhex('3ca7506212e8373b83b1da2ae6b291b995d4ad9a2220cd6f214bc18742d36882')
plaintext = "Coding crypto is really fun".encode()
iv = bytearray.fromhex('64833f8b4fa2da33b39ec9a48345a458')

# Cipher object to use
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

# encrypt
data = cipher.encrypt(pad(plaintext, AES.block_size))

iv = b64encode(cipher.iv).decode('utf-8')
ciphertext = b64encode(data).decode('utf-8')
# Save iv and ciphertext in json
iv_ciphertext_json = json.dumps({'iv':iv, 'ciphertext':ciphertext})
print(iv_ciphertext_json) 
