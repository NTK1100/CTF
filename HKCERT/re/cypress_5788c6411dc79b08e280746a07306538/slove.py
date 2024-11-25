import os
import requests
from Crypto.Cipher import AES
import hashlib

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

# Display c0, key, and iv for debugging
print("Server Response (c0):", c0.hex())
print("Generated Key:", key.hex())
print("Generated IV:", iv.hex())

# Attempt to decrypt c0 to recover the flag
# Create a new AES cipher for decryption
decrypt_cipher = AES.new(key, AES.MODE_CFB, iv=iv)
decrypted_flag = decrypt_cipher.decrypt(c0)

# Print the decrypted flag
print("Decrypted Flag:", decrypted_flag.decode(errors='ignore'))

# hkcert24{y0u_c4n_h00k_func710ns_t0_35c4p3_fr0m_r3v3r5e_3n9e3r1n9}
