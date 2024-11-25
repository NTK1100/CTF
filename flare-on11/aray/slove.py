# uint8(2) = 119 - 11
# uint32(3) = 2108416586 ^ 298697263
# uint8(7) = 82 + 15
# uint32(10) = 2448764514 -  383041523
# uint8(16) = 115 ^ 7
# uint32(17) = 1412131772 + 323157430
# uint8(21) = 94 + 21
# uint32(22) = 1879700858 ^ 372102464
# uint8(26) = 25 + 7
# uint8(27) = 40 ^ 21
# uint32(28) = 959764852 + 419186860
# uint8(36) = 72 - 4
# uint32(37) = 1228527996 - 367943707
# uint32(41) = 1699114335 - 404880684
# uint8(45) = 104 ^ 9
# uint32(46) = 1503714457 + 412326611
# uint32(52) = 1495724241 ^ 425706662
# uint8(58) = 122 -25
# uint32(59) = 1908304943 ^ 512952669
# uint8(65) = 70 + 29
# uint32(66) = 849718389 ^ 310886682
# uint32(70) = 2034162376 - 349203301
# uint8(74) = 116 - 11
# uint32(80) = 69677856 + 473886976
# uint8(84) = 128 -3

# Dữ liệu uint8
uint8_values = [
    (119 - 11),  # uint8(2)
    (82 + 15),   # uint8(7)
    (115 ^ 7),   # uint8(16)
    (94 + 21),   # uint8(21)
    (25 + 7),    # uint8(26)
    (40 ^ 21),   # uint8(27)
    (72 - 4),    # uint8(36)
    (104 ^ 9),   # uint8(45)
    (122 - 25),  # uint8(58)
    (70 + 29),   # uint8(65)
    (116 - 11),  # uint8(74)
    (128 - 3)    # uint8(84)
]

# Dữ liệu uint32
uint32_values = [
    (2108416586 ^ 298697263),
    (2448764514 - 383041523),
    (1412131772 + 323157430),
    (1879700858 ^ 372102464),
    (959764852 + 419186860),
    (1228527996 - 367943707),
    (1699114335 - 404880684),
    (1503714457 + 412326611),
    (1495724241 ^ 425706662),
    (1908304943 ^ 512952669),
    (849718389 ^ 310886682),
    (2034162376 - 349203301),
    (69677856 + 473886976)
]

result = ''.join(chr((value >> (8 * i)) & 0xFF) for value in uint32_values for i in range(4))

result += ''.join(chr(value) for value in uint8_values)

# In kết quả cuối cùng
print(result)