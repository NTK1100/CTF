# arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# print("".join(chr(a) for a in arr))


# flag = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# print(bytes.fromhex(flag))


# import base64
# flag ="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# print(base64.b64encode(bytes.fromhex(flag)))


# from Crypto.Util.number import long_to_bytes
# flag=11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print(long_to_bytes(flag))


# a="label"
# print("".join(chr(ord(i) ^ 13) for i in a))


# KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
# k1xork2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
# k2xork3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
# flagxored = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
# KEY2 = bytes(a ^ b for a,b in zip(KEY1, k1xork2))
# KEY3 = bytes(a ^ b for a,b in zip(KEY2, k2xork3))
# FLAG = bytes(a ^ b ^ c ^ d for a,b,c,d in zip(KEY1, KEY2, KEY3, flagxored))
# print(FLAG.decode())


# flag = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
# for i in range(1,20):
#     print(f"{i} >>> {"".join(chr(f ^ i) for f in flag)} {"\n"}")


# flag=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
# form= b"crypto{"
# key=[f ^ c for f,c in zip(form,flag)]+[flag[len(flag)-1] ^ ord('}')]
# print("".join(chr(f ^ key[i % len(key)]) for i, f in enumerate(flag)))



##########################################################    RSA//Diffie-Hellman   ###########################################################
from Cryptodome.Hash import SHA256
from Cryptodome.Util.number import * # type: ignore
import pwn
from sympy import factorint, mod_inverse
import telnetlib
import json
import base64
import binascii
from pwn import * # type: ignore
import codecs
import random
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib
import os

# n = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
# d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689

# hash = SHA256.new(data=b'crypto{Immut4ble_m3ssag1ng}')
# s = pow(bytes_to_long(hash.digest()), d, n)
# print(s)


#hàm inverse thuật toán Euclid mở rộng, hàm "inverse(g, p)" 
# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     gcd, x1, y1 = extended_gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd, x, y
# g = 209
# p = 991
# gcd, x, y = extended_gcd(g, p)
# d = x % p
# print(d)

# # Hàm phân tích thừa số nguyên tố của một số n
# def prime_factors(n):
#     i = 2
#     factors = []
#     # Kiểm tra các thừa số 2
#     while n % i == 0:
#         factors.append(i)
#         n //= i
#     i = 3
#     # Kiểm tra các thừa số lẻ từ 3 trở đi
#     while i * i <= n:
#         while (n % i == 0):
#             factors.append(i)
#             n //= i
#         i += 2
#     if n > 2:
#         factors.append(n)
#     return list(set(factors))  # Trả về danh sách các thừa số nguyên tố (loại bỏ phần tử trùng)

# # Hàm kiểm tra g có phải phần tử sinh không
# def is_primitive_root(g, p):
#     factors = prime_factors(p - 1)  # Lấy thừa số nguyên tố của (p-1)
    
#     # Kiểm tra g^((p-1)/q) mod p với mỗi q trong các thừa số nguyên tố
#     for q in factors:
#         if pow(g, (p - 1) // q, p) == 1:
#             return False
#     return True

# p = 28151

# # Duyệt qua các giá trị g từ 2 trở đi để tìm phần tử sinh
# for g in range(2, p):
#     if is_primitive_root(g, p):
#         print(g , p)
#         break

# g = 2
# p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

# A = 70249943217595468278554541264975482909289174351516133994495821400710625291840101960595720462672604202133493023241393916394629829526272643847352371534839862030410331485087487331809285533195024369287293217083414424096866925845838641840923193480821332056735592483730921055532222505605661664236182285229504265881752580410194731633895345823963910901731715743835775619780738974844840425579683385344491015955892106904647602049559477279345982530488299847663103078045601

# b = 12019233252903990344598522535774963020395770409445296724034378433497976840167805970589960962221948290951873387728102115996831454482299243226839490999713763440412177965861508773420532266484619126710566414914227560103715336696193210379850575047730388378348266180934946139100479831339835896583443691529372703954589071507717917136906770122077739814262298488662138085608736103418601750861698417340264213867753834679359191427098195887112064503104510489610448294420720

# B = 518386956790041579928056815914221837599234551655144585133414727838977145777213383018096662516814302583841858901021822273505120728451788412967971809038854090670743265187138208169355155411883063541881209288967735684152473260687799664130956969450297407027926009182761627800181901721840557870828019840218548188487260441829333603432714023447029942863076979487889569452186257333512355724725941390498966546682790608125613166744820307691068563387354936732643569654017172

# print(pow(A, b, p))

# def is_pkcs7_padded(message):
#     padding = message[-message[-1]:]
#     return all(padding[i] == len(padding) for i in range(0, len(padding)))


# def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
#     # Derive AES key from shared secret
#     sha1 = hashlib.sha1()
#     sha1.update(str(shared_secret).encode('ascii'))
#     key = sha1.digest()[:16]
#     # Decrypt flag
#     ciphertext = bytes.fromhex(ciphertext)
#     iv = bytes.fromhex(iv)
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     plaintext = cipher.decrypt(ciphertext)

#     if is_pkcs7_padded(plaintext):
#         return unpad(plaintext, 16).decode('ascii')
#     else:
#         return plaintext.decode('ascii')


# def main():
#     remote = pwn.remote("socket.cryptohack.org", 13371)

#     remote.recvuntil("Intercepted from Alice: ")
#     intercepted_from_alice = json.loads(remote.recvline())
#     intercepted_from_alice['p'] = "1"
#     remote.recvuntil("Send to Bob: ")
#     remote.sendline(json.dumps(intercepted_from_alice))

#     # We just forward Bobs request.
#     remote.recvuntil("Intercepted from Bob: ")
#     remote.sendline(remote.recvline())

#     remote.recvuntil("Intercepted from Alice: ")
#     alice_ciphertext = json.loads(remote.recvline())

#     shared_secret = 0
#     flag = decrypt_flag(shared_secret, alice_ciphertext["iv"], alice_ciphertext["encrypted_flag"])
#     pwn.log.info(flag)


# if __name__ == "__main__":
#     main()
