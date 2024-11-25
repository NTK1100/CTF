from sympy import mod_inverse

def elgamal_decrypt(encrypted_message, private_key):
    p, g, x = private_key
    decrypted_message = []

    for c1, c2 in encrypted_message:
        # Tính toán s = c1^x % p
        s = pow(c1, x, p)
        # Tính toán nghịch đảo của s
        s_inv = mod_inverse(s, p)
        # Giải mã ký tự
        m = (c2 * s_inv) % p
        decrypted_message.append(chr(m))  # Chuyển đổi về ký tự ASCII
    
    return ''.join(decrypted_message)

# Khóa bí mật và thông điệp mã hóa
private_key = (157, 27, 74)
encrypted_message = [
    (156, 67), (67, 129), (101, 122), (93, 38), (111, 43), (93, 135), (99, 65), (1, 65),
    (93, 2), (82, 74), (16, 83), (56, 74), (16, 144), (130, 87), (99, 65), (39, 63), (16, 62),
    (67, 50), (1, 72), (118, 63), (93, 26), (56, 83), (58, 41), (46, 113), (143, 140), (118, 122),
    (108, 32), (75, 153), (93, 54), (93, 2), (141, 41), (1, 78), (14, 92), (67, 117), (93, 38),
    (118, 67), (108, 102), (27, 9), (67, 8), (101, 125), (101, 53), (141, 15), (58, 26), (14, 66),
    (49, 139), (27, 94), (14, 24), (27, 50), (39, 156), (118, 70), (82, 99), (4, 66), (99, 30),
    (90, 153), (49, 102), (27, 50), (56, 66), (4, 63), (64, 128)
]

# Giải mã thông điệp
decrypted_text = elgamal_decrypt(encrypted_message, private_key)
print(f"Decrypted text: {decrypted_text}")
