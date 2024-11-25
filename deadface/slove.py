def encrypt(v30, v24):
    v26 = [0] * 512
    v13 = 0
    v14 = 0
    v19 = 0
    ArgList = [0] * (len(v24) + 1)  # Độ dài của ArgList dựa trên v24

    # Khởi tạo mảng v26
    for k in range(256):
        v26[k] = k
        v26[k + 256] = v30[k & 0xF]  # v30 là một chuỗi có 16 ký tự

    # Hoán vị mảng v26
    for m in range(256):
        v17 = v26[m]
        v13 = (v17 + v26[m + 256] + v13) % 256
        v18 = v26[v13]
        v26[v13] = v17
        v26[m] = v18

    # XOR với v24 để tạo ra ArgList
    for n in range(len(v24)):  # Điều chỉnh vòng lặp theo độ dài của v24
        v14 = (v14 + 1) % 256
        v21 = v26[v14]
        v19 = (v21 + v19) % 256
        v22 = v26[v19]
        v26[v19] = v21
        v26[v14] = v22
        ArgList[n] = v24[n] ^ v26[(v22 + v26[v19]) % 256]

    ArgList[len(v24)] = 0  # Kết thúc chuỗi bằng ký tự NULL

    # Xuất kết quả ArgList
    return ''.join(chr(c) for c in ArgList[:len(v24)])

# Ví dụ dữ liệu input
v24 = [0x6B, 0xDD, 0x92, 0xEE, 0x7A, 0x58, 0x95, 0x44, 0x65, 0x5A, 0xB5, 0xA6, 0xB3, 0xF5, 0x62, 0xB2]
v30 = [0x57, 0xA2, 0x86, 0xC3, 0x63, 0xD9, 0x00, 0x65, 0xBA, 0xEB, 0x1E, 0xEB, 0xCB, 0xAB, 0x5A, 0xAE]

# Mã hóa/giải mã
result = encrypt(v30, v24)
print(result)
