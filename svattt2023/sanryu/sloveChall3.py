def rotation(a, n):
    n = n % 8
    return ((a >> n) | (a << (8 - n))) & 0xFF

cipher = [0xD7, 0x9E, 0xCA, 0x51, 0xA4, 0xEB, 0x8A, 0x48, 0x2B, 0xBE, 0x62, 0x04, 0x96, 0x2B, 0xD7, 0x11, 0xDB, 0x63, 0xFA]
rol = [0xF3A8D24E, 0x57286251, 0xED0BB215, 0xC54297C6, 0x1372D3D1, 0x9AEBB2FD, 0x4074858D, 0xD8F50000, 0x95E8F163, 0x325640E9,
       0x6C750331, 0x86A54774, 0xD88DDA56, 0xFBD660C5, 0x77F4124E, 0x9077A73E, 0xB8817C4E, 0xB4A4110C, 0xBC4E8A99]

flag = ""
for i in range(0, 19):
    flag += chr(rotation(cipher[i], rol[i]))

print(flag)