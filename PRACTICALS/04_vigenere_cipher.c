#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void){char text[1000],key[1000];printf("Plaintext: ");fgets(text,sizeof text,stdin);printf("Keyword: ");scanf("%999s",key);
 int j=0;for(int i=0;text[i];i++)if(isalpha((unsigned char)text[i])){int base=islower((unsigned char)text[i])?'a':'A';text[i]=(char)(base+(text[i]-base+(toupper((unsigned char)key[j++%strlen(key)])-'A'))%26);}
 printf("Ciphertext: %s",text);return 0;}
