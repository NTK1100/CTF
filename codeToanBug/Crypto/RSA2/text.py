from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

secret_key = get_random_bytes(16)
cipher_aes = AES.new(secret_key, AES.MODE_CBC)
iv = cipher_aes.iv

encrypted_private_key = cipher_aes.encrypt(pad(private_key, AES.block_size))

flag = b'flag'
cipher_rsa = PKCS1_OAEP.new(key.publickey())
ciphertext = cipher_rsa.encrypt(flag)

with open('secret_key.bin', 'wb') as f:
    f.write(secret_key)

with open('iv.bin', 'wb') as f:
    f.write(iv)

with open('private', 'wb') as f:
    f.write(encrypted_private_key)

with open('encrypt_flag', 'wb') as f:
    f.write(ciphertext)

with open('publickey.pem', 'wb') as f:
    f.write(public_key)

print(f"IV: {binascii.hexlify(iv).decode()}")
print(f"Encrypted Private Key (AES): {binascii.hexlify(encrypted_private_key).decode()}")
print(f"Encrypted Flag: {binascii.hexlify(ciphertext).decode()}")
print(f"Public Key: {public_key.decode()}")
