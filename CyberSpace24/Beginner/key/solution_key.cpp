#include <iostream>

int main() {
    int v6[32] = {67, 164, 65, 174, 66, 252, 115, 176, 111, 114, 94, 168, 101, 242, 81, 206,
                  32, 188, 96, 164, 109, 70, 33, 64, 32, 90, 44, 82, 45, 94, 45, 196};

    for (int i = 0; i < 32; ++i) {
        for(int f=1; f<1000; ++f){
            if(((i % 2 + 1) * (i ^ f))==v6[i]){
                std::cout << f << " ";
                break;
            }
        }
    }
    return 0;
}
//CSCTF{u_g0T_it_h0OrAy6778462123}