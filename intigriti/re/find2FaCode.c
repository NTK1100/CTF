#include <stdint.h>
#include <stdio.h>

// Hàm dịch vòng trái 32-bit
uint32_t rol4(uint32_t value, int count) {
    count %= 32; // Đảm bảo dịch trong phạm vi 32 bit
    return (value << count) | (value >> (32 - count));
}

// Hàm obscure_key
uint32_t obscure_key(uint32_t a1) {
    return (4919 * rol4(a1 ^ 0xA5A5A5A5, 3)) ^ 0x5A5A5A5A;
}

// Hàm generate_2fa_code
uint32_t generate_2fa_code(int a1) {
    uint32_t v4 = 48879 * a1;
    uint32_t v3 = 48879 * a1;

    for (int i = 0; i <= 9; ++i) {
        v4 = obscure_key(v4); // Cập nhật giá trị v4
        v3 = ((v4 >> (i % 5)) ^ (v4 << (i % 7))) + rol4(v4 ^ v3, 5);
    }
    return v3 & 0xFFFFFF; // Chỉ giữ lại 24 bit cuối
}

// Hàm main để kiểm tra
int main() {
    int a1 = 1337; // Giá trị đầu vào
    uint32_t result = generate_2fa_code(a1);
    printf("Generated 2FA code: %06X\n", result); // In kết quả 6 ký tự hex
    return 0;
}
