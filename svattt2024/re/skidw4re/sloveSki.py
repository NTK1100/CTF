from Crypto.Cipher import AES

key = b"thisis32bitlongpassphraseimusing"
ciphertext = bytes.fromhex("ae385c6f1dd72132b2afcd4c25b9d35e")


cipher = AES.new(key, AES.MODE_ECB)


decrypted_message = cipher.decrypt(ciphertext)

print(decrypted_message.decode())