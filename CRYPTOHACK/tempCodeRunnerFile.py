#hàm inverse thuật toán Euclid mở rộng
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
g = 209
p = 991
gcd, x, y = extended_gcd(g, p)
d = x % p
print(d)