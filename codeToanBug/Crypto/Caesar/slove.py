def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():  
            start = ord('A') if char.isupper() else ord('a')
            
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            result += char  

    return result

# Chuỗi cần so sánh
target_text = "FRGH_WRDQ_EXJ{O-dev-v0-Hdvb-b0-xFdq-v0oyH.}"

# Thử tất cả các giá trị shift từ 1 đến 25
for shift_value in range(1, 26):
    decrypted_text = caesar_encrypt(target_text, -shift_value)
    print(f"Shift: {shift_value}, Decrypted text: {decrypted_text}")
