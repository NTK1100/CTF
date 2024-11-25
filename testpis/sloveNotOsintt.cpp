#include <iostream>

int main() {
    // Khởi tạo mảng a2 với các giá trị đã cho
    int a2[23] = {34, 17, 31, 103, 59, 92, 3, 48, 67, 30, 62, 18, 28, 33, 49, 33, 9, 4, 29, 38, 54, 75, 70};
    
    // Khởi tạo mảng a1 với chuỗi "PTITInformationSecurity"
    char a1[24] = "PTITInformationSecurity";

    // Khởi tạo mảng a3 và thực hiện phép XOR
    char a3[23];
    for (int i = 0; i < 23; ++i) {
        a3[i] = a2[i] ^ a1[i];
    }

    // In ra các ký tự ASCII tương ứng với giá trị trong mảng a3
    std::cout << "Các ký tự ASCII của a3 là: ";
    for (int i = 0; i < 23; ++i) {
        std::cout << a3[i];
    }
    std::cout << std::endl;

    return 0;
}
//PIS{rEV3r2e_1s_fuN_rlghT_??}