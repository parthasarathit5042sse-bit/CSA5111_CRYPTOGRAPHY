#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void) {
    char text[1000]; int k;
    printf("Enter plaintext: "); if (!fgets(text, sizeof text, stdin)) return 1;
    printf("Enter shift (1-25): "); if (scanf("%d", &k) != 1) return 1;
    k = ((k % 26) + 26) % 26;
    for (int i=0; text[i]; i++) {
        if (isupper((unsigned char)text[i])) text[i] = 'A' + (text[i]-'A'+k)%26;
        else if (islower((unsigned char)text[i])) text[i] = 'a' + (text[i]-'a'+k)%26;
    }
    printf("Ciphertext: %s", text);
    return 0;
}
