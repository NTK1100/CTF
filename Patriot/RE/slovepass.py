# import os
# import secrets
# from base64 import b64encode

# def promptGen():
#     # Hàm lambda để tăng giá trị ASCII của từng ký tự
#     flipFlops = lambda x: ''.join(chr(ord(c) + 1) for c in x)

#     with open('topsneaky.txt', 'rb') as f:
#         first = f.read()

#     # Tạo một chuỗi ngẫu nhiên có cùng độ dài với nội dung của tệp
#     bittys = secrets.token_bytes(len(first))

#     # Thực hiện XOR giữa dữ liệu tệp và chuỗi ngẫu nhiên
#     onePointFive = int.from_bytes(first, 'big') ^ int.from_bytes(bittys, 'big')

#     # Chuyển kết quả XOR về dạng byte
#     second = onePointFive.to_bytes(len(first), 'big')

#     # Mã hóa base64 và giải mã sang chuỗi utf-8
#     third = b64encode(second).decode('utf-8')

#     # Mã hóa bittys thành base64
#     bittysEnc = b64encode(bittys).decode('utf-8')

#     # Thực hiện phép biến đổi bằng hàm flipFlops
#     fourth = ''.join(flipFlops(each) for each in third)

#     # Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp   Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV
#     fifth = f"Mwahahaha you will n{fourth[:10]}ever crack into my pass{fourth[10:]}word, i'll even give you the key and the executable:::: {bittysEnc}"
    
#     return fifth

# def main():
#     print(promptGen())

# if __name__ == '__main__':
#     main()
from base64 import b64decode

# Chuỗi đã có sẵn
fourth = "Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp"
bittysEnc = "Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"

# 2. Đảo ngược hàm flipFlops
reverseFlipFlops = lambda x: ''.join(chr(ord(c) - 1) for c in x)

# 1. Giải mã base64 cho fourth
reversed_fourth = reverseFlipFlops(fourth)
print(f"Reversed fourth: {reversed_fourth}")

# 2. Giải mã base64 cho fourth đã đảo
decoded_fourth = b64decode(reversed_fourth)

# 3. Giải mã base64 cho bittysEnc
bittys = b64decode(bittysEnc)
print(f"Decoded bittys: {bittys}")

# 4. Chuyển reversed_fourth thành bytes
reversed_fourth_bytes = reversed_fourth.encode('utf-8')

# XOR reversed_fourth với bittys để tìm first
first_bytes = bytes([b1 ^ b2 for b1, b2 in zip(decoded_fourth, bittys)])

# 5. In ra first dưới dạng các ký tự ASCII
first_ascii = first_bytes.decode('utf-8', errors='ignore')  # Bỏ qua các ký tự không hợp lệ
print(f"First (ASCII): {first_ascii}")

