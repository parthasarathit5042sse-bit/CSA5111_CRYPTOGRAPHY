#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void) {
    char text[1000], key[27];
    printf("Enter 26-letter substitution alphabet (e.g. QWERTYUIOPASDFGHJKLZXCVBNM): ");
    if (scanf("%26s", key)!=1 || strlen(key)!=26) return 1;
    int seen[26]={0};
    for(int i=0;i<26;i++){ key[i]=(char)toupper((unsigned char)key[i]); if(key[i]<'A'||key[i]>'Z'||seen[key[i]-'A']++) {puts("Invalid key: use each A-Z exactly once.");return 1;} }
    getchar(); printf("Enter plaintext: "); if(!fgets(text,sizeof text,stdin)) return 1;
    for(int i=0;text[i];i++){ if(isupper((unsigned char)text[i])) text[i]=key[text[i]-'A']; else if(islower((unsigned char)text[i])) text[i]=(char)tolower(key[text[i]-'a']); }
    printf("Ciphertext: %s",text); return 0;
}
