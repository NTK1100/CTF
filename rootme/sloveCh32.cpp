#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

// Hàm chuyển chuỗi thành mảng byte
void string_to_byte_array(const char *str, uint8_t *buf, size_t buf_len) {
    size_t str_len = strlen(str);
    if (str_len > buf_len) {
        str_len = buf_len; // Đảm bảo không ghi quá giới hạn bộ đệm
    }
    memcpy(buf, str, str_len);
}

// Hàm so sánh hai mảng byte
int compare_bytes(const uint8_t *arr1, const uint8_t *arr2, size_t len) {
    for (size_t i = 0; i < len; i++) {
        if (arr1[i] != arr2[i]) {
            return 0; // Không khớp
        }
    }
    return 1; // Khớp
}

int main() {
    const char *s = "rootme";
    uint8_t buf[32] = {0}; // Bộ đệm để lưu chuỗi đã chuyển đổi
    uint8_t v17[32] = {0}; // Mảng v17
    uint8_t v3[32];        // Mảng v3 là copy của v17
    uint8_t array[32] = {0}; // Mảng kết quả
    size_t v2 = sizeof(v17); // Kích thước của v17
    size_t v7;
    
    // Chuyển chuỗi thành mảng byte
    string_to_byte_array(s, buf, sizeof(buf));

    // Copy v17 sang v3
    memcpy(v3, v17, v2);

    // Vòng lặp chính để XOR từng byte
    for (size_t i = 0; i < v2; i++) {
        if (strlen((char*)buf) == 0) {
            printf("Error: runtime_panicdivide (divide by zero)\n");
            exit(1);
        }

        // Tính chỉ số v7
        if (strlen((char*)buf) == -1) {
            v7 = 0;
        } else {
            v7 = i % strlen((char*)buf);
        }

        // Kiểm tra chỉ số hợp lệ
        if (v7 >= strlen((char*)buf) || i >= sizeof(array)) {
            printf("Error: runtime_panicindex (index out of bounds)\n");
            exit(1);
        }

        // XOR giữa phần tử v3 và byte từ "rootme"
        array[i] = buf[v7] ^ v3[i];
    }

    // So sánh kết quả với mảng mong đợi (giả sử mảng mong đợi là all-zero)
    uint8_t expected_result[32] = {0}; // Giả sử mảng kết quả mong đợi là toàn 0
    if (compare_bytes(array, expected_result, v2)) {
        printf("Match found!\n");
    } else {
        printf("No match.\n");
    }

    return 0;
}
