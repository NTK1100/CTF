#include <windows.h>
#include <stdio.h>
#include <wincrypt.h>

int main() {
    HCRYPTPROV hProv;
    HCRYPTKEY hKey;
    HCRYPTHASH hHash;
    DWORD dwBufLen;
    BYTE pbData[24];
    
    // Mảng chứa các giá trị mã hóa (v12) bạn cung cấp
    DWORD v12[7] = {
        0x8688FC48, 0x8B6EAB89, 0x82519474, 0xA7DA51A4,
        0x9827EFA0, 0xE4D30302, 0xD6B9EDFA
    };

    // Chuỗi "warmup_challenge" để tạo khóa
    strcpy((char *)pbData, "warmup_challenge");

    // 1. Khởi tạo ngữ cảnh mã hóa
    if (!CryptAcquireContext(&hProv, NULL, NULL, PROV_RSA_AES, CRYPT_VERIFYCONTEXT)) {
        printf("Error during CryptAcquireContext.\n");
        return 1;
    }

    // 2. Tạo đối tượng hash
    if (!CryptCreateHash(hProv, CALG_SHA1, 0, 0, &hHash)) {
        printf("Error during CryptCreateHash.\n");
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    // 3. Hash chuỗi "warmup_challenge"
    if (!CryptHashData(hHash, pbData, strlen((char *)pbData), 0)) {
        printf("Error during CryptHashData.\n");
        CryptDestroyHash(hHash);
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    // 4. Tạo khóa từ hash
    if (!CryptDeriveKey(hProv, CALG_RC4, hHash, 0, &hKey)) {  // CALG_RC4 là thuật toán mã hóa được giả định ở đây
        printf("Error during CryptDeriveKey.\n");
        CryptDestroyHash(hHash);
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    // 5. Giải mã dữ liệu (v12)
    dwBufLen = sizeof(v12);  // Kích thước của dữ liệu cần giải mã
    if (!CryptDecrypt(hKey, 0, TRUE, 0, (BYTE *)v12, &dwBufLen)) {
        printf("Error during CryptDecrypt.\n");
        CryptDestroyKey(hKey);
        CryptDestroyHash(hHash);
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    // 6. In chuỗi sau khi giải mã
    printf("Decrypted data: %s\n", (char *)v12);

    // 7. Dọn dẹp tài nguyên
    CryptDestroyKey(hKey);
    CryptDestroyHash(hHash);
    CryptReleaseContext(hProv, 0);

    return 0;
}
//CIS2024{900dw0rk_foR_w4RmUp}