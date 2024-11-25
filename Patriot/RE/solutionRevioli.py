#PCTF{ITALY_01123581321345589144233377}
def calc(a1):
    if a1 == 0:
        return 0
    if a1 == 1:
        return 1
    
    v3 = 0
    v4 = 1
    for i in range(2, a1 + 1):
        v5 = v3 + v4
        v3 = v4
        v4 = v5
    
    return v4

# Tạo mảng v4 chứa các số Fibonacci từ 0 đến 14
v4 = [calc(i) for i in range(15)]

# Biến dest dùng để chứa chuỗi kết quả
dest = ""

for j in range(15):  
    s = f"{v4[j]}"  
    dest += s      

print("Chuỗi kết quả:", dest)
