#include <math.h>
#include <stdio.h>
#include <string.h>

unsigned __int64 tetra(unsigned int a1, int a2) {
    double v2;
    int i;
    unsigned __int64 v5 = (unsigned int)a1; // Sử dụng unsigned int để tránh cảnh báo

    // Tính lũy thừa và điều chỉnh giá trị trong vòng lặp
    for (i = 0; i < a2 - 1; ++i) {
        v2 = pow(a1, v5); // Tính lũy thừa
        if (v2 >= 9.223372036854776e18) {
            v5 = (unsigned __int64)(v2 - 9.223372036854776e18) ^ 0x8000000000000000ULL;
        } else {
            v5 = (unsigned __int64)v2; // Chuyển đổi về unsigned __int64
        }
    }

    return v5; // Trả về giá trị tính toán
}

int main(int argc, const char **argv, const char **envp) {
    int i, j, k;
    int v7[4];  // Mảng 4 phần tử
    const char *aRedacted = "REDACTED";  // Chuỗi REDACTED thay placeholder

    // Gọi hàm tetra và lưu kết quả vào mảng v7
    for (i = 1; i <= 4; ++i) {
        v7[i - 1] = tetra(2u, i) % 0x13; // Lưu kết quả vào mảng
    }

    // In giá trị trong mảng v7
    for (j = 0; j < 4; ++j) { // Sửa chỉ số từ <= 3 thành < 4
        printf("%d ", v7[j]);
    }

    // XOR các ký tự trong "REDACTED" với giá trị trong mảng v7
    for (k = 0; k < strlen(aRedacted); ++k) {
        printf("%x", v7[k % 4] ^ (unsigned char)aRedacted[k]); // Chuyển đổi về unsigned char
    }

    putchar(10); // Xuống dòng
    return 0;
}
