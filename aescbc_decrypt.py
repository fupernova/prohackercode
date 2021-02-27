import json
import sys
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Run 'python3 aescbc_decrypt.py ciphertext.json key.txt'

# Need 3 arguments
if len(sys.argv) < 3:
    print("hoi")
    sys.exit(1)
#Get ciphertext json file    
ciphertextFile = open(sys.argv[1], "r")

ivCiphertextInJson = json.loads(ciphertextFile.read())

# Get key file
keyFile = open(sys.argv[2], "r")
key = bytearray.fromhex(keyFile.read())

iv = b64decode(ivCiphertextInJson['iv'])
ciphertext = b64decode(ivCiphertextInJson['ciphertext'])
# Cipher object to use
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(plaintext)

