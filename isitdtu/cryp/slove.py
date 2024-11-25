import hashlib
import random
import string

# Tiền tố cho bài toán PoW
prefix = "JKq30mKOLlgSJvbb"
target = "000000"

def find_suffix():
    while True:
        # Tạo chuỗi ngẫu nhiên dài 8 ký tự để thử làm suffix
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        # Tạo kết quả băm SHA-256 cho chuỗi `prefix + suffix`
        hash_result = hashlib.sha256((prefix + suffix).encode()).hexdigest()
        
        # Kiểm tra nếu băm bắt đầu với '000000'
        if hash_result.startswith(target):
            return suffix, hash_result

# Tìm suffix
suffix, hash_result = find_suffix()
print(f"Found suffix: {suffix}")
print(f"SHA256 hash: {hash_result}")
