#include <bits/stdc++.h>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void* my_memfrob(void* s, size_t n) {
    unsigned char* p = static_cast<unsigned char*>(s);
    for (size_t i = 0; i < n; ++i) {
        p[i] ^= 0x2A;
    }
    return s;
}

unsigned int rot_n(unsigned int hexChar, int shift) {
    char a1 = static_cast<char>(hexChar);

    if (isalpha(a1)) {  
        char base = isupper(a1) ? 'A' : 'a';
        char rotated = (a1 - base + shift + 26) % 26 + ba--se;  
        return static_cast<unsigned int>(rotated);
    }
    return hexChar;
}

int main() {
    char check[] = {0x5f, 0x40, 0x5a, 0x15, 0x75, 0x45, 0x62, 0x53, 0x75, 0x46, 0x52, 0x43, 0x5f, 0x75, 0x50, 0x52, 0x75, 0x5f, 0x5c, 0x4f};
    char s1[sizeof(check)];
    int v6;

    my_memfrob(check, strlen(check));

    for (int i = 0; i < strlen(check); ++i) {
        int j=4*i;
        while(!is_prime(j)){
            ++j;
        }
        s1[i] = rot_n(check[i],-j);
    }
    s1[strlen(check)] = '\0';
    cout << "s1: " << s1 << endl;
    return 0;
}