#include <stdio.h>
#include <ctype.h>
int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
int main(void){char s[1000];int a,b;printf("Enter a and b (a must be coprime to 26): ");if(scanf("%d%d",&a,&b)!=2)return 1;if(gcd((a%26+26)%26,26)!=1){puts("Invalid a: gcd(a,26) must be 1. b may be any integer.");return 1;}getchar();printf("Plaintext: ");fgets(s,sizeof s,stdin);for(int i=0;s[i];i++)if(isalpha((unsigned char)s[i])){int base=islower((unsigned char)s[i])?'a':'A';s[i]=(char)(base+((a*(s[i]-base)+b)%26+26)%26);}printf("Ciphertext: %s",s);return 0;}
