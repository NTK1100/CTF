input_file_path = 'C:\\Users\\Admin\\Downloads\\ctfptithn\\7Z\\new_tonton.png'
output_file_path = 'C:\\Users\\Admin\\Downloads\\ctfptithn\\7Z\\flag.png'

# Đọc dữ liệu từ file gốc
with open(input_file_path, 'rb') as file:
    data = file.read()

# Chuyển đổi dữ liệu thành bytearray để dễ dàng thao tác
reversed_data = bytearray(data)

# Đảo từng cặp byte
for i in range(0, len(reversed_data) - 1, 2):
    reversed_data[i], reversed_data[i + 1] = reversed_data[i + 1], reversed_data[i]

# Ghi dữ liệu đã đảo vào file mới
with open(output_file_path, 'wb') as output_file:
    output_file.write(reversed_data)

print(f"Dữ liệu đã được đảo và ghi vào {output_file_path}")
