#include <stdio.h>
#include <stdlib.h>

int main() {
    setbuf(stdout, NULL);
    int so1, so2;

    printf("Nhap gia tri so thu nhat: ");
    scanf("%d", &so1);
    
    if (so1 < 0) {
        printf("Noooooo");
        return 1;
    }

    printf("Nhap gia tri so thu hai: ");
    scanf("%d", &so2);

    if (so2 < 0) {
        printf("Noooooo");
        return 1;
    }
    printf("...............................\n");
    
    int sum = so1 + so2;

    printf("Tong hai so la: %d\n", sum);

    if (sum < 0) {
        printf(":(\n");
        system("/bin/cat flag.txt");
    } else {
        printf("Byeeeeee!");
    }

    return 0;
}
