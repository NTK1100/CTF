import base64

# Thông tin từ mã gốc
srt_key = 'secretkey'
output = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="

# 1. Giải mã Base64
decoded_val = base64.b64decode(output).decode()

# 2. Khôi phục giá trị ban đầu từ XOR
output_arr = list(decoded_val)
usr_input_half_len = len(output_arr) // 2
usr_input = []

for i in range(usr_input_half_len):
    enc_p1 = output_arr[2 * i]    # Ký tự đầu tiên của cặp
    enc_p2 = output_arr[2 * i + 1]  # Ký tự thứ hai của cặp

    # Khôi phục c1 và c2 bằng cách XOR với khóa bí mật
    c1 = chr(ord(enc_p1) ^ ord(srt_key[i % len(srt_key)]))
    c2 = chr(ord(enc_p2) ^ ord(srt_key[i % len(srt_key)]))

    # Thêm c1 và c2 vào chuỗi kết quả
    usr_input.append(c1)  # Đây là phần chuỗi ban đầu
    usr_input.insert(0, c2)  # Đây là phần của chuỗi đã đảo ngược

# Ghép lại chuỗi ban đầu
original_input = ''.join(usr_input)
print("Input ban đầu:", original_input)
