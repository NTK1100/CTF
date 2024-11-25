#include <iostream>
#include <vector>
#include <iomanip> // Thêm thư viện này để dùng setw và setfill

int main() {
    // Mảng kết quả sau khi qua các phép XOR
    std::vector<uint16_t> a = {
        0xD99C, 0xA9DD, 0xD98C, 0xA9CA, 0xD99D, 0xA9CF, 0xD9B2, 0xA9FA, 0xD9F8, 0xA9E4, 0xD9B9, 0xA9E5, 0xD9FA, 0xA9D6, 0xD9AF, 0xA9E5, 0xD9FD, 0xA9EE, 0xD996, 0xD9EF, 0xA9F9, 0xD9FB, 0xA996, 0xD9DA, 0xA9BD, 0xD9BD, 0xA9BB, 0xD9FD, 0xA9AC, 0xD9DB, 0xA9B4
    };

    // Bước 1: XOR ngược lại với 0x1337
    for (size_t i = 0; i < a.size(); ++i) {
        a[i] ^= 0x1337;
    }

    // Bước 2: XOR ngược lại với 0xBABE và 0xCAFE dựa trên chỉ số lẻ/chẵn
    for (int i = 0; i <= 30; ++i) {
        if (i & 1) {
            a[i] ^= 0xBABE; // Chỉ số lẻ XOR ngược lại với 0xBABE
        } else {
            a[i] ^= 0xCAFE; // Chỉ số chẵn XOR ngược lại với 0xCAFE
        }
    }

    // In ra kết quả, tức là input ban đầu
    std::cout << "Input ban đầu:\n";
    for (size_t i = 0; i < a.size(); ++i) {
        std::cout << std::hex << std::setw(4) << std::setfill('0') << a[i] << " ";
        //UTECTF{s1mpl3_fl4g_pfp0prp_pSptp4prptpepRp}
    }

    return 0;
}
