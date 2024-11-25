import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def create_sha256_hash(a: int, b: int) -> bytes:
    combined_string = str(a) + str(b)
    sha256_hash = hashlib.sha256(combined_string.encode()).digest()
    return sha256_hash

def aes_decrypt(encrypted_data: str, key: bytes) -> str:
    try:
        # Giải mã Base64 để lấy dữ liệu mã hóa nhị phân
        encrypted_data = base64.b64decode(encrypted_data)

        # Tách IV và dữ liệu mã hóa
        iv = encrypted_data[:16]  # IV là 16 byte đầu tiên
        encrypted_data = encrypted_data[16:]  # Dữ liệu mã hóa là phần còn lại
        
        # Giải mã dữ liệu
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        
        # Trả về dữ liệu đã giải mã dưới dạng chuỗi
        return decrypted_data.decode()
    except (ValueError, KeyError) as e:
        print(f"Error during decryption: {e}")
        return ""

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def find_all_solutions(p, q, d):
    gcd, x0, y0 = extended_gcd(p, q)
    
    if d % gcd != 0:
        raise ValueError("d không phải là bội số của gcd(p, q)")

    # Nhân với hệ số d // gcd
    x0 *= d // gcd
    y0 *= d // gcd

    # Tìm bước điều chỉnh
    q_div_gcd = q // gcd
    p_div_gcd = p // gcd

    solutions = []

    # Điều chỉnh để a >= 0
    if x0 < 0:
        k = (-x0 + q_div_gcd - 1) // q_div_gcd
        x0 += k * q_div_gcd
        y0 -= k * p_div_gcd

    # Điều chỉnh để b >= 0
    if y0 < 0:
        k = (-y0 + p_div_gcd - 1) // p_div_gcd
        x0 -= k * q_div_gcd
        y0 += k * p_div_gcd

    # Điều chỉnh để a và b không vượt quá 2^64 - 1
    k_min = 0
    k_max = (2**64 - 1 - x0) // q_div_gcd

    for k in range(k_min, k_max + 1):
        a = x0 + k * q_div_gcd
        b = y0 - k * p_div_gcd
        if 0 <= b <= 2**64 - 1:
            solutions.append((a, b))

    return solutions

# Giá trị p, q, và d được cung cấp
p = 8951710828661776134393557345559872811359525081937041878826708239020667692635062064920564714607104340890226533416992454355108122227572711169555760176210615
q = 1794203726060135253359412584688493132438925104900230683035683265166991717384266772144007067935000288473079526287603528986038228900040559111698310257014564
d = 167478740517820226468457218015029944569141475452167655461038612860456186852651031117450824272004497064830485255993006471616399836695888469339053542709671363258119855205392426

# Tìm tất cả các giá trị a và b
solutions = find_all_solutions(p, q, d)

# In ra tất cả các giải pháp
for a, b in solutions:
    
    # Sử dụng các giá trị `a` và `b` đã tính toán
    key = create_sha256_hash(a, b)
    encrypted_data = "bb4zVtYWJJm9lxUR7UdxJ6GumSNhqnREfvUoRhKv0V4wEBjIgSKXwBkceJjZ1zUO"
    decrypted = aes_decrypt(encrypted_data, key)
    print("Decrypted data:", decrypted)
