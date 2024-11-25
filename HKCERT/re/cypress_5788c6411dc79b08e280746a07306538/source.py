import os
import requests
from Crypto.Cipher import AES
import hashlib

# Prompt the user to enter the flag
flag = input("What is the flag?> ").encode()

# Function to generate a nonce
def get_nonce():
    while True:
        nonce = os.urandom(16)
        hash_val = hashlib.sha256(b"pow/" + nonce).digest()
        if hash_val[:3] == b"\x00\x00\x00":  # Condition to check hash prefix
            return nonce

# Generate nonce
nonce = get_nonce()

# Make a POST request to the server with the nonce
url = 'https://c12-cypress.hkcert24.pwnable.hk/'
response = requests.post(url, json={"nonce": nonce.hex()})

# Convert the server response to bytes
c0 = bytes.fromhex(response.text)

# Generate encryption key and IV
key = hashlib.sha256(b"key/" + nonce).digest()[:16]
iv = hashlib.sha256(b"iv/" + nonce).digest()[:16]

# Create an AES cipher in CFB mode and encrypt the flag
cipher = AES.new(key, AES.MODE_CFB, iv=iv)
c1 = cipher.encrypt(flag)

# Print a result based on comparison
print("🙆🙅"[c0 != c1])
