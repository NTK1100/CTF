# #!/usr/bin/env python3

# from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

# e = 3
# d = -1

# while d == -1:
#     p = getPrime(1024)
#     q = getPrime(1024)
#     phi = (p - 1) * (q - 1)
#     d = inverse(e, phi)

# n = p * q

# flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
# pt = bytes_to_long(flag)
# ct = pow(pt, e, n)

# print(f"n = {n}")
# print(f"e = {e}")
# print(f"ct = {ct}")

# pt = pow(ct, d, n)
# decrypted = long_to_bytes(pt)
# assert decrypted == flag

from Cryptodome.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from sympy import mod_inverse, factorint
from gmpy2 import * # type: ignore
e = 3
c = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
# căn bậc e của c trả về [index, true/false], [0] trả về index, [1] trả về true/false
print(bytes.fromhex(hex(iroot(c, e)[0])[2:])) # type: ignore