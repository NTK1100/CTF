# Dữ liệu enc_flag được cung cấp dưới dạng chuỗi hex
enc_flag_hex = "74784B6577485C69687E5C79776246797705465473725969687E5C7E5A61576A77665A5202625C79775C007C570D0D4D"

# Chuyển đổi từ chuỗi hex sang mảng byte
enc_flag_bytes = bytes.fromhex(enc_flag_hex)

# Thử XOR từng byte với chiều dài len
# Ở đây giả sử len = len(enc_flag_bytes)
length = len(enc_flag_bytes)
decoded_flag = bytes([b ^ length for b in enc_flag_bytes])

# Chuyển mảng byte kết quả thành chuỗi
decoded_flag.decode(errors="replace"), decoded_flag

print(decoded_flag)
