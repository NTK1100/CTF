from sympy import mod_inverse, isprime, primerange
import random

def generate_prime(bits=8):
    primes = list(primerange(2**(bits-1), 2**bits))
    return random.choice(primes)

def elgamal_key_generation(bits=8):
    p = generate_prime(bits)
    g = random.randint(2, p-1)
    x = random.randint(1, p-2)
    y = pow(g, x, p)
    return (p, g, y), (p, g, x)

def elgamal_encrypt(message, public_key):
    p, g, y = public_key
    encrypted_message = []
    
    for m in message:
        k = random.randint(1, p-2)
        c1 = pow(g, k, p)
        c2 = (ord(m) * pow(y, k, p)) % p
        encrypted_message.append((c1, c2))
    
    return encrypted_message


public_key, private_key = elgamal_key_generation(bits=8)


flag = "flag"
encrypted_text = elgamal_encrypt(flag, public_key)


print(f"public key: {public_key}")
print(f"private key: {private_key}")
print(f"encrypted text: {encrypted_text}")