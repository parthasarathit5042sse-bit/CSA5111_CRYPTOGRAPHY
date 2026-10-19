#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void){int a=9,b=4,c=5,d=7; /* key interpreted as [[9,4],[5,7]] from the provided stacked values 94 / 57 */char s[1000],p[1000];int n=0;printf("Plaintext: ");fgets(s,sizeof s,stdin);for(int i=0;s[i];i++)if(isalpha((unsigned char)s[i]))p[n++]=toupper((unsigned char)s[i]);if(n%2)p[n++]='X';printf("Ciphertext: ");for(int i=0;i<n;i+=2){int x=p[i]-'A',y=p[i+1]-'A';putchar('A'+(a*x+b*y)%26);putchar('A'+(c*x+d*y)%26);}puts("");puts("Note: decryption requires an invertible key matrix modulo 26; this key's determinant is 43 ≡ 17 (mod 26), which is invertible.");return 0;}
