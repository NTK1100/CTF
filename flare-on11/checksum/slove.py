import base64

f = b'FlareOn2024'
x = base64.b64decode("cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA==")

flag = "".join(chr(x[i] ^ f[i % len(f)]) for i in range(len(x)))

print(flag)
