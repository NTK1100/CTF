def generate_key(D, length):
    """Tạo khóa từ danh sách các số D với độ dài cho trước."""
    key = []
    for i in range(length):
        key.append(D[i % len(D)])
    return key

def xor(F, D):
    """Mã hóa hoặc giải mã nội dung F bằng khóa D."""
    key = generate_key(D, len(F))
    G = []
    
    for i in range(len(F)):
        GChar = F[i] ^ key[i]
        G.append(GChar)
        
    return G

def main():
    # Đầu vào E được mã hóa (danh sách các số nguyên biểu diễn bằng hex)
    E_hex = ['0x3F', '0x5F', '0x22', '0x20', '0x32', '0x13', '0x12', '0x00', '0x25', '0x33', '0x5D', '0x2A', 
             '0x30', '0x4E', '0x07', '0x46', '0x55', '0x1A', '0x36', '0x1C', '0x5A', '0x1E', '0x07', '0x42', 
             '0x3E', '0x1F', '0x54', '0x0A', '0x0B', '0x36', '0x1C', '0x27', '0x01', '0x5B', '0x13', '0x50', 
             '0x11', '0x1B', '0x3A', '0x02', '0x25', '0x1A', '0x58', '0x40', '0x1C', '0x1A', '0x1D', '0x54', 
             '0x04', '0x1C', '0x36', '0x22', '0x5B', '0x35', '0x23', '0x54', '0x1C']
    E = [int(x, 16) for x in E_hex]  # Chuyển từ hex sang decimal

    # Khóa D (danh sách các giá trị ASCII từ chuỗi D_hex)
    D_hex = "whatthehelldoyouthinkyouaredoing"
    D = [ord(x) for x in D_hex]  # Chuyển từ chuỗi thành danh sách giá trị ASCII
    
    # Giải mã để tìm nội dung C
    decoded_list = xor(E, D)
    
    # Chuyển danh sách các giá trị ASCII thành chuỗi ký tự
    decoded = ''.join([chr(x) for x in decoded_list])
    
    print("Decoded: ", decoded)

if __name__ == "__main__":
    main()
