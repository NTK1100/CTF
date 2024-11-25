from sympy import mod_inverse

def rsa_key_generation(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = 65537 
    d = mod_inverse(e, phi_n)
    
    return (e, n), d 

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in plaintext]
    return encrypted


p = 61  
q = 53
public_key, private_key = rsa_key_generation(p, q)

flag = "flag"
encrypted_text = rsa_encrypt(flag, public_key)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Encrypted text: {encrypted_text}")
