key = [73, 83, 80, 67, 84, 70, 50, 48, 50, 52]
input_file_path = 'C:\\Users\\Admin\\Downloads\\pisctf\\RE1\\ISPCTF2024.png'
output_file_path = 'C:\\Users\\Admin\\Downloads\\pisctf\\RE1\\flag.png'

with open(input_file_path, 'rb') as file:
    data = file.read()

    decrypted_data = bytearray(data)
    print(decrypted_data[0])
    for i in range(len(key)):
        for j in range(len(data)):
            decrypted_data[j] ^= key[i]

with open(output_file_path, 'wb') as output_file:
    output_file.write(decrypted_data)