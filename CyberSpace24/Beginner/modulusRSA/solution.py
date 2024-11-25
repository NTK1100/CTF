from sympy import isprime, nextprime
from sympy.ntheory import factorint

# Dữ liệu đầu vào
w = 115017953136750842312826274882950615840
x = 16700949197226085826583888467555942943
y = 20681722155136911131278141581010571320

# Tìm giá trị p
diff_px = abs(x - w)
possible_ps = [i for i in factorint(diff_px) if isprime(i)]

# Tìm giá trị q
diff_qy = abs(y - r)
possible_qs = [i for i in factorint(diff_qy) if isprime(i)]

def find_valid_primes(possible_ps, possible_qs):
    for p in possible_ps:
        for q in possible_qs:
            if p != q:
                r_candidates = [i for i in range(y, y + 100) if i % q == y]
                for r in r_candidates:
                    if r % p == x:
                        return p, q, r
    return None, None, None

p, q, r = find_valid_primes(possible_ps, possible_qs)

if p and q and r:
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"r = {r}")
else:
    print("Không tìm thấy các số nguyên tố phù hợp.")
