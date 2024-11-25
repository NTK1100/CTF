#include <stdio.h>
#include <windows.h>

int main()
{
    HMODULE hModule = LoadLibrary("C:\\Users\\Admin\\Downloads\\ctf\\dreamhack\\re\\Inject ME\\prob_rev.dll");
    if (hModule == NULL)
    {
        printf("Failed to load DLL. Error: %d\n", GetLastError());
        return 1;
    }
    printf("DLL loaded successfully.\n");
    // Giữ chương trình chạy để kiểm tra.
    getchar();
    FreeLibrary(hModule);
    return 0;
}
