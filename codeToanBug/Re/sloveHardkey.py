import math

def is_prime(a1):
    if a1 <= 1:
        return False
    for i in range(2, int(math.sqrt(a1)) + 1):
        if a1 % i == 0:
            return False
    return True

def next_prime(a1):
    while True:
        a1 += 1
        if is_prime(a1):
            return a1

def validate_input(a1, a2, a3):
    for i in range(a2):
        prime = next_prime(a1)
        a1 = (1 << (i % 8)) ^ (((( (a3 + prime * a1) >> 31) >> 24) + a3 + prime * a1) - (((a3 + prime * a1) >> 31) >> 24))
    return a1 == 42

# Thiết lập khoảng tìm kiếm cho a1, a2, và a3 (ví dụ: từ 0 đến 255)
for a1 in range(256):
    for a2 in range(1, 10):  # Giới hạn a2 để tránh vòng lặp quá dài
        for a3 in range(256):
            if validate_input(a1, a2, a3):
                print(f"Tìm thấy giá trị: a1 = {a1}, a2 = {a2}, a3 = {a3}")
                break
