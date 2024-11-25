# def main():
#     s = input("Input: ")
#     v9 = [""] * 3  # Mảng để lưu ba chuỗi

#     # Phân tách chuỗi
#     for i in range(3):
#         for j in range(i, len(s), 3):
#             v9[i] += s[j]  # Lưu ký tự vào phần tương ứng của v9

#     dest = "".join(v9)  # Ghép các chuỗi lại với nhau
#     print("Output:", dest)

# if __name__ == "__main__":
#     main()
# Các chuỗi đầu vào
a = "HT859092947c8"
b = "7F4cff7727181"
c = "C{872a2ba640}"

# Ghép các ký tự từ ba chuỗi
result = []
length = min(len(a), len(b), len(c))  # Đảm bảo vòng lặp không vượt quá chiều dài của chuỗi ngắn nhất

for i in range(length):
    result.append(a[i])  # Thêm ký tự từ chuỗi a
    result.append(b[i])  # Thêm ký tự từ chuỗi b
    result.append(c[i])  # Thêm ký tự từ chuỗi c

# Chuyển danh sách thành chuỗi
final_result = ''.join(result)

print("Kết quả:", final_result)