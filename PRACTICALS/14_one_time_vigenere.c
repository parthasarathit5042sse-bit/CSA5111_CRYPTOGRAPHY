#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void){char s[1000];int key[1000],n=0,k;printf("Plaintext (letters/spaces): ");fgets(s,sizeof s,stdin);printf("Enter key numbers for each letter, then -1 to finish:\n");while(n<999&&scanf("%d",&k)==1&&k!=-1){if(k<0||k>25){puts("Key values must be 0..25.");return 1;}key[n++]=k;}int j=0;printf("Ciphertext: ");for(int i=0;s[i];i++){if(isalpha((unsigned char)s[i])){int base=islower((unsigned char)s[i])?'a':'A';if(j>=n){puts("\nNot enough key values.");return 1;}putchar(base+((s[i]-base+key[j++])%26));}else putchar(s[i]);}puts("");return 0;}
