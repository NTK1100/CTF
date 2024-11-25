#can you inspect the web?, something is hidden there! (>.o)
chars = open("decrypt.py", 'r').read()

lookup = "\n \"\'#(){}*+/0123456789:=_.,[]abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

out = ""

prev = 0

for char in chars:
  cur = lookup.index(char)
  out += lookup[(cur - prev) % 81]
  prev = cur
  
with open("ciphertext", "w") as file:
  file.write(out)