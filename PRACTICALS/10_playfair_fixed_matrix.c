#include <stdio.h>
#include <ctype.h>
#include <string.h>
char sq[5][5]={{'M','F','H','I','K'},{'U','N','O','P','Q'},{'Z','V','W','X','Y'},{'E','L','A','R','G'},{'D','S','T','B','C'}};
void pos(char c,int *r,int *k){if(c=='J')c='I';for(int i=0;i<5;i++)for(int j=0;j<5;j++)if(sq[i][j]==c){*r=i;*k=j;return;}}
int main(void){char in[1000],p[1000],out[1000];int n=0;printf("Message: ");fgets(in,sizeof in,stdin);for(int i=0;in[i];i++)if(isalpha((unsigned char)in[i]))p[n++]=toupper((unsigned char)in[i]);for(int i=0;i<n;){if(i+1<n&&p[i]==p[i+1]){memmove(p+i+2,p+i+1,n-i);p[i+1]='X';n++;}i+=2;}if(n%2)p[n++]='X';for(int i=0;i<n;i+=2){int r,c,s,t;pos(p[i],&r,&c);pos(p[i+1],&s,&t);if(r==s){out[i]=sq[r][(c+1)%5];out[i+1]=sq[s][(t+1)%5];}else if(c==t){out[i]=sq[(r+1)%5][c];out[i+1]=sq[(s+1)%5][t];}else{out[i]=sq[r][t];out[i+1]=sq[s][c];}}out[n]=0;printf("Ciphertext: %s\n",out);return 0;}
