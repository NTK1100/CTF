def rsa_decrypt(ciphertext, private_key, n):
    decrypted = [chr(pow(c, private_key, n)) for c in ciphertext]
    return ''.join(decrypted)

# Danh sách input được mã hóa
ciphertext = [641, 1307, 1759, 28, 119, 2159, 1307, 2790, 3165, 119, 524, 2310, 669, 855, 3123, 1086, 487, 1086, 1859, 1230, 2790, 1086, 1230, 2680, 2170, 1759, 1759, 1086, 2170, 1632, 2170, 1632, 2170, 3000, 3000, 1516]

# Giả sử bạn đã có các giá trị d và n
d = 2753  # Khóa bí mật
n = 3233  # n = p * q

# Giải mã
decrypted_text = rsa_decrypt(ciphertext, d, n)
print(f"Decrypted text: {decrypted_text}")
