#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void){char s[4000];printf("Enter affine ciphertext: ");fgets(s,sizeof s,stdin);
 /* Try every valid affine key; inspect candidate plaintexts manually. */
 for(int a=1;a<26;a++){int g=a;while(g){int t=26%g;26=g;g=t;} /* reset below */ 
  int x=a,y=26;while(y){int t=x%y;x=y;y=t;}if(x!=1)continue;
  int inv=1;while((a*inv)%26!=1)inv++;
  for(int b=0;b<26;b++){printf("a=%d b=%d: ",a,b);for(int i=0;s[i];i++){if(isalpha((unsigned char)s[i])){int base=islower((unsigned char)s[i])?'a':'A';putchar(base+((inv*((s[i]-base-b+26*2)%26))%26));}else putchar(s[i]);}puts("");}
 }return 0;}
