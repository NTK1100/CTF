import hashlib
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

a, b = random.randint(0, 2**64), random.randint(0, 2**64)
p, q = random.randint(0, 2**512), random.randint(0, 2**512)

d = a * p + b * q
print(f'{p = }\n{q = }\n{d = }')

def create_sha256_hash(a: int, b: int) -> bytes:
    combined_string = str(a) + str(b)
    sha256_hash = hashlib.sha256(combined_string.encode()).digest()
    return sha256_hash

def aes_encrypt(data: str, key: bytes) -> str:
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
    encrypted_data_with_iv = iv + encrypted_data
    return base64.b64encode(encrypted_data_with_iv).decode()

flag = "PIS{fake_flag}"
key = create_sha256_hash(a, b)
encrypted = aes_encrypt(flag, key)

print("Encrypted data:", encrypted)


# p = 8951710828661776134393557345559872811359525081937041878826708239020667692635062064920564714607104340890226533416992454355108122227572711169555760176210615
# q = 1794203726060135253359412584688493132438925104900230683035683265166991717384266772144007067935000288473079526287603528986038228900040559111698310257014564
# d = 167478740517820226468457218015029944569141475452167655461038612860456186852651031117450824272004497064830485255993006471616399836695888469339053542709671363258119855205392426
# Encrypted data: bb4zVtYWJJm9lxUR7UdxJ6GumSNhqnREfvUoRhKv0V4wEBjIgSKXwBkceJjZ1zUO