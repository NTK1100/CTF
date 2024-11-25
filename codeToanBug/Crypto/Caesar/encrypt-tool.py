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



plain_text = "flag"
shift_value = 3

encrypted_text = caesar_encrypt(plain_text, shift_value)
print(f"plain text encrypted: {encrypted_text}")
