#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void xor_encrypt(unsigned long long *data, char *key, size_t len) {
    size_t key_len = strlen(key);
    
    // XOR từng byte của dữ liệu với khóa
    for (size_t i = 0; i < len; i++) {
        ((char*)data)[i] ^= key[i % key_len];
    }
}

int print_flag() {
    char v1[13]; // Mảng lưu key
    unsigned long long v2[3]; // Dữ liệu để giải mã
    unsigned long long v3[3]; // Một phần khác của dữ liệu (không dùng để in flag)

    // Khởi tạo dữ liệu mã hóa (được XOR)
    v2[0] = 0x1317111E3438292DLL;
    v2[1] = 0x1150162C1C161911LL;
    v2[2] = 0x404423F3A1F4717LL;

    // Khởi tạo một mảng dữ liệu khác (không liên quan tới flag)
    v3[0] = 0x54181A513B1A302DLL;
    *(((unsigned int *)((char *)v3 + 7))) = 407121236;

    // Chuỗi khóa để XOR
    strcpy(v1, "keysecretkey");

    // Giải mã dữ liệu bằng cách XOR với khóa
    xor_encrypt(v2, v1, 35LL);

    // In flag đã giải mã
    return printf("Password correct, please see flag: %s\n", (char *)v2);
}

bool check_password(const char *a1) {
    if (strlen(a1) != 10)
        return false;
    if (a1[0] != 114 || a1[1] != 101)
        return false;
    if (a1[2] != 112 || a1[3] != 97)
        return false;
    if (a1[4] != 115 || a1[5] != 115)
        return false;
    if (a1[6] != 119 || a1[7] != 111)
        return false;
    return a1[8] == 114 && a1[9] == 100;
}

int main() {
    const char *password = "repassword";

    if (check_password(password)) {
        printf("Password is correct!\n");
    } else {
        printf("Password is incorrect.\n");
    }

     print_flag();
    return 0;

    return 0;
}
