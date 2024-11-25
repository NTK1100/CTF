def find_valid_input():
    a1 = [''] * 8  # Khởi tạo chuỗi a1 với 8 ký tự

    for i in range(8):
        # Tính toán giá trị cần có để thỏa mãn điều kiện
        target_value = i * i + 3
        a1[i] = chr(target_value ^ (i + 85))

    return ''.join(a1)

# Kiểm tra đầu ra
valid_input = find_valid_input()
print(f"Chuỗi hợp lệ là: {valid_input}")
