import binascii
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Run 'python3 aescbc_encrypt.py > ciphertext.json'

# Set up key, plaintext and iv
key = bytearray.fromhex('ca64e7ca9072688df97616cf67417ea0e5d7d3470ca34037fb3ae7dfd750ad75')
plaintext = "I really really hate crypto".encode()
iv = bytearray.fromhex('6de5f9be2d8349d726fb54d0742dfbdb')

# Cipher object to use
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

# encrypt
data = cipher.encrypt(pad(plaintext, AES.block_size))

iv = b64encode(cipher.iv).decode('utf-8')
# ciphertext = b64encode(data).decode('utf-8')
ciphertext = b64encode(data).decode('utf-8')
# Save iv and ciphertext in json
iv_ciphertext_json = json.dumps({'iv':iv, 'ciphertext':ciphertext})
print(iv_ciphertext_json)

print("\nOutput in hex:")
decode_text = b64decode(ciphertext).hex()
print(decode_text)
