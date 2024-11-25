# Khai báo giá trị mảng v6 và khởi tạo các tệp cần thiết
v6 = [0xDE, 0xAD, 0xBE, 0xEF]

# Mở tệp encrypted để đọc và tệp decrypted để ghi kết quả
with open("encrypted", "rb") as encrypted_file, open("decrypted.png", "wb") as decrypted_file:
    v5 = 0  # Biến đếm số byte đã xử lý
    while byte := encrypted_file.read(1):  # Đọc từng byte từ tệp
        # Giải mã byte và đảm bảo giá trị trong khoảng 0-255
        decoded_byte = ((ord(byte) - 19) ^ v6[v5 % 4]) % 256
        # Ghi byte đã giải mã vào tệp
        decrypted_file.write(bytes([decoded_byte]))
        v5 += 1
