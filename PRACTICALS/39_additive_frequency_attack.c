#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void){char s[4000];printf("Enter additive/shift ciphertext: ");fgets(s,sizeof s,stdin);for(int k=0;k<26;k++){printf("Shift %2d: ",k);for(int i=0;s[i];i++){char c=s[i];if(isupper((unsigned char)c))putchar('A'+(c-'A'-k+26)%26);else if(islower((unsigned char)c))putchar('a'+(c-'a'-k+26)%26);else putchar(c);}puts("");}return 0;}
