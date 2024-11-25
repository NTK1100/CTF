values = [74, 51, 83, 81, 68, 127, 39, 61, 100, 97, 114, 102, 55, 49, 33, 100, 51, 98, 34, 48, 59, 53, 33, 54, 103, 48, 40, 53, 55, 98, 113, 52, 58, 55, 117, 53, 48, 48, 109]
xor_values = [2, 4, 16, 5]

result = []
for i in range(len(values)):
    # Lấy chỉ số của giá trị xor
    xor_index = i % len(xor_values)
    # Thực hiện phép XOR
    result_value = values[i] ^ xor_values[xor_index]
    result.append(result_value)

print(result)
