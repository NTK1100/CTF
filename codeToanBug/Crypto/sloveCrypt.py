def decrypt_variable_shift(encrypted_message):
    decrypted = []
    
    for index, char in enumerate(encrypted_message):
        shift_amount = -(index + 1)  # Dịch ngược lại theo vị trí (index + 1)
        
        if char.isalpha():
            if char.isupper():
                # Xử lý ký tự in hoa
                new_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            elif char.islower():
                # Xử lý ký tự in thường
                new_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            decrypted.append(new_char)
        else:
            # Giữ nguyên các ký tự không phải chữ cái
            decrypted.append(char)
    
    return ''.join(decrypted)

# Chuỗi mã hóa
encrypted_message = "VXB{Nzy1_Mm4g_B7j}"

# Giải mã với dịch chuyển thay đổi theo vị trí
decrypted_message = decrypt_variable_shift(encrypted_message)
print("Giải mã:", decrypted_message)
