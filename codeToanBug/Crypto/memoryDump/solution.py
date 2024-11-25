import struct

def to_32bit_blocks(values):
    while len(values) % 4 != 0:
        values.append(0)
    blocks = []
    for i in range(0, len(values), 4):
        block = struct.unpack('>I', bytes(values[i:i + 4]))[0]
        blocks.append(block)
    return blocks


def from_32bit_blocks(blocks):
    values = []
    for block in blocks:
        bytes_block = struct.pack('>I', block)
        values.extend(bytes_block)
    return values


def ror32(value, shift):
    shift &= 31
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF


def rol32(value, shift):
    shift &= 31
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF


def xor32(value1, value2):
    return (value1 ^ value2) & 0xFFFFFFFF


def reg_encrypt(block, key):
    for i in range(0, 3):
        # block = ror32(block, 1)
        block = xor32(block, key)
    return block


def reg_decrypt(block, key):
    for i in range(0, 3):
        block = xor32(block, key)
        # block = rol32(block, 1)
    return block

def decrypt(key, blocks):
    key_value = key
    result = []
    for block in blocks:
        decrypted_block = reg_decrypt(block, key_value)
        result.append(decrypted_block)
        key_value = decrypted_block
    return result

encrypted_blocks = [
    0xD68C2DDA ,0x4D115F42, 0x721D2A00, 0x0745681C, 0x0C454800, 0x79631E29, 0x650C2409, 0x140D0B11, 0x040B1B1C
]

initial_key = 0xABAD1DEA

decrypted_blocks = decrypt(initial_key, encrypted_blocks)

result = from_32bit_blocks(decrypted_blocks)
decrypted_text = ''.join(map(chr, result)).rstrip('\x00')[::-1]

print(f"Giải mã được chuỗi: {decrypted_text}")