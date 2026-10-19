#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void){char s[4000];int count[26]={0};const char *eng="ETAOINSHRDLCUMWFGYPBVKJXQZ";printf("Enter substitution ciphertext: ");fgets(s,sizeof s,stdin);
 for(int i=0;s[i];i++)if(isalpha((unsigned char)s[i]))count[toupper((unsigned char)s[i])-'A']++;
 int order[26];for(int i=0;i<26;i++)order[i]=i;
 for(int i=0;i<26;i++)for(int j=i+1;j<26;j++)if(count[order[j]]>count[order[i]]){int t=order[i];order[i]=order[j];order[j]=t;}
 char map[26];for(int i=0;i<26;i++)map[order[i]]=eng[i];
 puts("Frequency-based candidate (heuristic; substitution cracking needs language scoring for reliable results):");
 for(int i=0;s[i];i++){char c=s[i];if(isupper((unsigned char)c))putchar(map[c-'A']);else if(islower((unsigned char)c))putchar(tolower(map[c-'a']));else putchar(c);}puts("");
 puts("Cipher letter counts:");for(int i=0;i<26;i++)printf("%c:%d%c",'A'+i,count[i],i==25?'\n':' ');return 0;}
