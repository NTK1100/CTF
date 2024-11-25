import base64
import zlib

def decode_base64_and_decompress(data):
    try:
        # Giải mã Base64
        decoded_data = base64.b64decode(data)
        # Giải nén bằng zlib
        decompressed_data = zlib.decompress(decoded_data)
        return decompressed_data.decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

# Các chuỗi bạn đã cung cấp
title = "eJyLdyoyCMlI1Q1ycFBUBAAcgAOm"
subject = "eJxzzHP0iSzJdA4Ojo+P9zMo0XVKdKkFAEztBvw="
keywords = "eJxz9ndxjQ/xd/SLdwp1r47Mz9E1MNAFAEdDBlM="

print("Title:", decode_base64_and_decompress(title))
print("Subject:", decode_base64_and_decompress(subject))
print("Keywords:", decode_base64_and_decompress(keywords))
