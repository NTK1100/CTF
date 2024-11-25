# Chuỗi hex ban đầu
hex_string = "7e54595f09434b0f4a5d59757b514a5b6d550d0f0c765b7d45"

# Ký tự XOR
xor_char = "8"

# Chuyển ký tự XOR sang giá trị số nguyên
xor_value = ord(xor_char)

# Chuyển chuỗi hex thành mảng byte
byte_array = bytes.fromhex(hex_string)

# Thực hiện XOR từng byte với xor_value
result = bytes(b ^ xor_value for b in byte_array)

# Chuyển kết quả sang ASCII
try:
    result_ascii = result.decode("ascii")  # Giải mã mảng byte thành chuỗi ASCII
except UnicodeDecodeError:
    result_ascii = "Kết quả chứa các ký tự không thể in được."

# In kết quả dạng hex và ASCII
print(result_ascii)
# Flag1{s7reaMCircUm574NcE}

# Dữ liệu mã hóa (hex)
encoded_hex = "775a5051034d5644706002635f467d0570030558454b"

# Khóa XOR
key = "16"

# Chuyển đổi dữ liệu hex thành byte
encoded_data = bytes.fromhex(encoded_hex)

# Giải mã dữ liệu bằng cách XOR với khóa
key_bytes = key.encode()  # Chuyển khóa thành dạng byte
decoded_data = bytes(encoded_data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(encoded_data)))

# Chuyển kết quả về ASCII (nếu các byte có thể hiển thị)
try:
    decoded_string = decoded_data.decode("ascii")
except UnicodeDecodeError:
    decoded_string = decoded_data  # Nếu có lỗi giải mã, in ra byte nguyên bản

# In kết quả
print(decoded_string)
# Flag2{grAV3UnpL3A54nt}

# Chuỗi hex đã mã hóa
hex_encoded = "755e525500496177065b057c076602025d6152467a0755735046025d5d4f"

# Khóa XOR
key = "32"

# Chuyển đổi hex thành mảng byte
encoded_bytes = bytes.fromhex(hex_encoded)

# Tìm input gốc bằng cách XOR với khóa
key_bytes = key.encode()  # Chuyển khóa sang dạng byte
decoded = bytes(encoded_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(encoded_bytes)))

# Chuyển kết quả về ASCII
decoded_string = decoded.decode("ascii")  # Chuỗi ASCII thu được

# In kết quả
print(decoded_string)
# Flag3{RE5i6N4T10nSatI5fAct1on
