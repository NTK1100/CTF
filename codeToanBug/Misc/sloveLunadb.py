from datetime import datetime, timezone

def time(time):
# 1681578000 là số giây kể từ 1/1/1970
    date = datetime.fromtimestamp(time, timezone.utc)  # Chuyển thành UTC
    return date.strftime("%d/%m/%Y-%H:%M:%S")

import struct
import hashlib

# Hàm để tính băm SHA-256
def hash_password(password):
    return hashlib.sha256(password).digest()

# Hàm đọc 1 Byte
def read_byte(file):
    return struct.unpack('B', file.read(1))[0]

# Hàm đọc 2 Bytes (Short)
def read_short(file):
    return struct.unpack('H', file.read(2))[0]

# Hàm đọc 4 Bytes (Int)
def read_int(file):
    return struct.unpack('I', file.read(4))[0]

# Hàm đọc 8 Bytes (Long)
def read_long(file):
    return struct.unpack('Q', file.read(8))[0]

# Hàm đọc ULEB128 (số nguyên độ dài thay đổi)
def read_uleb128(file):
    result = 0
    shift = 0
    while True:
        byte = read_byte(file)
        result |= (byte & 0x7F) << shift
        if (byte & 0x80) == 0:
            break
        shift += 7
    return result

# Hàm đọc String theo định dạng LunaDB
def read_string(file):
    prefix = read_byte(file)
    if prefix == 0x00:
        return None
    elif prefix == 0x0b:
        length = read_uleb128(file)
        return file.read(length).decode('utf-8')
    else:
        raise ValueError("Invalid string prefix")

# Hàm đọc Byte String theo định dạng LunaDB
def read_byte_string(file):
    prefix = read_byte(file)
    if prefix == 0x00:
        return None
    elif prefix == 0x0c:
        length = read_uleb128(file)
        return file.read(length)
    else:
        raise ValueError("Invalid byte string prefix")

def read_person(file):
    person_id = read_short(file)
    first_name = read_string(file)
    last_name = read_string(file)
    username = read_string(file)
    password_hash = read_byte_string(file)
    email = read_string(file)
    account_created = read_long(file)
    permission = read_byte(file)
    is_active = bool(read_byte(file))
    last_modified = read_long(file)

    return {
        "ID": person_id,
        "First Name": first_name,
        "Last Name": last_name,
        "Username": username,
        "Password Hash": password_hash,
        "Email": email,
        "Account Created": account_created,
        "Permission": permission,
        "Is Active": is_active,
        "Last Modified": last_modified,
    }

def check_permission(permission):
    if permission == 1:
        return "r"
    elif permission == 2:
        return "w"
    elif permission == 3:
        return "rw"
    elif permission == 4:
        return "x"
    elif permission == 5:
        return "rx"
    elif permission == 6:
        return "wx"
    elif permission == 7:
        return "rwx"
    else:
        return "No valid permission"

def read_database(file_path):
    target_password_hash = hash_password(b"How can you find this")

    with open(file_path, 'rb') as file:
        # Đọc Magic Header
        magic = file.read(4)
        if magic != b'LUNA':
            raise ValueError("Not a valid LunaDB file")

        # Đọc tên cơ sở dữ liệu
        db_name = read_string(file)

        # Đọc phiên bản cơ sở dữ liệu
        db_version = read_int(file)

        # Đọc tên tổ chức
        organization_name = read_string(file)

        # Đọc số lượng người dùng
        num_rows = read_int(file)

        # Đọc từng người dùng và in ra
        for _ in range(num_rows):
            person = read_person(file)

            # So sánh băm mật khẩu
            if person['Password Hash'] == target_password_hash:
                # In theo định dạng yêu cầu
                print(f"{person['ID']} {person['First Name']} {person['Last Name']} {person['Username']} {person['Password Hash']} {person['Email']} {person['Account Created']} {person['Permission']} {person['Is Active']} {person['Last Modified']}")
                print(f"{"CODE_TOAN_BUG{"}{person['Username']}{"_"}{time(person['Account Created'])}{"_"}{time(person['Last Modified'])}{"_"}{check_permission(person["Permission"])}{"}"}")

file_path = 'C:\\Users\\Admin\\Downloads\\ctf\\codeToanBug\\Misc\\940def114033_database.lunadb'
db_data = read_database(file_path)