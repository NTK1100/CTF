def rowena_rawenclaw_diadem(s, shift):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            if 'A' <= char <= 'Z':
                base = 'A'
            else:
                base = 'a'
            shifted = (ord(char) - ord(base) - shift + 26) % 26 + ord(base)
            result += chr(shifted)
        else:
            result += char
    return result

# Giá trị đầu vào
a1 = "K7FWI{"
a2 = 3

# Gọi hàm và in kết quả
modified_string = rowena_rawenclaw_diadem(a1, a2)
print("Kết quả:", modified_string)
import base64

def marvolo_gaunt_ring(encoded_str):
    # Giải mã Base64, chuyển đổi từ bytes sang chuỗi ký tự ASCII
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_str = decoded_bytes.decode('ascii')
        return decoded_str
    except Exception as e:
        return str(e)  # Trả về thông báo lỗi nếu có

# Chuỗi đã mã hóa Base64
a1 = "JW4wdyFuZ18A"

# Gọi hàm và in kết quả
decoded_string = marvolo_gaunt_ring(a1)
print("Chuỗi giải mã:", decoded_string)

def nagini(a1, a2):
    i = 0
    while i < len(a1) and a1[i] != 0:
        a1[i] ^= a2
        i += 1
    return a1

# Chuẩn bị dữ liệu đầu vào
a1_hex = 0x122729262E686F2A
a2 = 75  # Giá trị XOR là 75

# Chuyển giá trị hex thành bytearray
a1_bytes = bytearray(a1_hex.to_bytes((a1_hex.bit_length() + 7) // 8, 'big'))

# Gọi hàm và in kết quả
result_bytes = nagini(a1_bytes, a2)

# In kết quả dưới dạng chuỗi ASCII
print("Kết quả sau XOR (ASCII):", result_bytes.decode('ascii'))

def slytherin_locket(s, a2):
    length = len(s)  # Chiều dài chuỗi s
    src = [''] * length  # Tạo một danh sách ký tự để giữ kết quả tạm thời
    
    index = 0  # Biến index dùng để kiểm soát các vị trí ghi vào src
    # Vòng lặp qua từng "hàng"
    for i in range(a2):
        step = 2 * (a2 - 1)  # Khoảng cách giữa các ký tự ở cùng một hàng
        # Vòng lặp để xếp các ký tự vào src
        for j in range(i, length, step):
            if index < length:  # Kiểm tra để tránh tràn chuỗi
                src[index] = s[j]
                index += 1
            # Thêm ký tự tại vị trí đối xứng qua trung điểm của hàng
            if i != 0 and i != a2 - 1 and (j + 2 * i < length):
                if index < length:
                    src[index] = s[j + 2 * i]
                    index += 1
    
    # Chuyển danh sách ký tự trở lại thành chuỗi và trả về
    return ''.join(src)

# Giá trị đầu vào và gọi hàm
v7 = "m$43_k"
result = slytherin_locket(v7, 3)
print("Kết quả:", result)

def hufflepuff_cup(a1):
    v3 = len(a1)  # Độ dài của chuỗi
    a1_list = list(a1)  # Chuyển chuỗi thành danh sách để dễ dàng thay đổi ký tự

    # Đảo ngược chuỗi
    for i in range(v3 // 2):
        # Hoán đổi ký tự
        a1_list[i], a1_list[v3 - 1 - i] = a1_list[v3 - 1 - i], a1_list[i]

    # Chuyển danh sách trở lại thành chuỗi
    reversed_string = ''.join(a1_list)
    return reversed_string, v3  # Trả về chuỗi đã đảo và độ dài

# Giá trị đầu vào
a1 = "_gn1h7yr5ve"

# Gọi hàm và in kết quả
result_string, length = hufflepuff_cup(a1)
print("Chuỗi đã đảo:", result_string)
def tom_riddle_diary(a1):
    result = ""
    
    for char in a1:
        if char == '\0':  # Kiểm tra ký tự kết thúc chuỗi
            break
        if ord(char) <= 64 or ord(char) > 90:
            if 'a' <= char <= 'z':
                # Chuyển ký tự thường theo quy tắc
                new_char = chr((ord(char) - 84) % 26 + ord('a'))
            else:
                new_char = char  # Nếu không phải ký tự a-z thì giữ nguyên
        else:
            # Chuyển ký tự hoa theo quy tắc
            new_char = chr((ord(char) - 52) % 26 + ord('A'))

        result += new_char  # Nối ký tự mới vào kết quả

    return result

# Giá trị đầu vào
a1 = "0c3a_"

# Gọi hàm và in kết quả
encoded_string = tom_riddle_diary(a1)
print("Chuỗi mã hóa:", encoded_string)
def harry_potter(a1, a2, a3):
    v8 = len(a1)  # Độ dài của chuỗi a1
    v7 = len(a2)  # Độ dài của chuỗi a2
    result = []   # Danh sách để lưu trữ kết quả
    v9 = 0        # Biến đếm cho a2

    for v10 in range(v8):  # Duyệt qua từng ký tự trong a1
        char = a1[v10]

        # Kiểm tra xem ký tự có phải là chữ cái không
        if char.isalpha():
            if char.isupper():
                v3 = 'A'  # Nếu là chữ hoa
            else:
                v3 = 'a'  # Nếu là chữ thường
            
            # Tính toán chỉ số và mã hóa
            v4 = ord(char) - ord(v3)
            encoded_char = (v4 - (ord(a2[v9 % v7]) - ord('A')) + 26) % 26 + ord(v3)
            result.append(chr(encoded_char))  # Thêm ký tự đã mã hóa vào kết quả
            
            v9 += 1  # Tăng biến đếm
        else:
            result.append(char)  # Nếu không phải chữ cái, thêm ký tự gốc vào kết quả

    # Kết quả cuối cùng
    return ''.join(result)

# Giá trị đầu vào
a1 = "$0yeev!}"
a2 = "ENCRYPT"
a3 = 0  # Địa chỉ không cần thiết trong Python, sẽ bỏ qua

# Gọi hàm và in kết quả
encoded_string = harry_potter(a1, a2, a3)
print("Chuỗi mã hóa:", encoded_string)
