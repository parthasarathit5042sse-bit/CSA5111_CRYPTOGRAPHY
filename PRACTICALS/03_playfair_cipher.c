#include <stdio.h>
#include <ctype.h>
#include <string.h>
void makeSquare(const char *key,char sq[5][5]){
 int used[26]={0},n=0; char all[100]; snprintf(all,sizeof all,"%sABCDEFGHIJKLMNOPQRSTUVWXYZ",key);
 for(int i=0;all[i];i++){char c=(char)toupper((unsigned char)all[i]); if(c<'A'||c>'Z')continue; if(c=='J')c='I'; if(!used[c-'A']){used[c-'A']=1;sq[n/5][n%5]=c;n++;}}
}
void pos(char sq[5][5],char c,int *r,int *col){if(c=='J')c='I';for(int i=0;i<5;i++)for(int j=0;j<5;j++)if(sq[i][j]==c){*r=i;*col=j;return;}}
int main(void){
 char key[100],in[1000],p[2000],out[2000],sq[5][5]; int n=0;
 printf("Keyword: ");scanf("%99s",key); getchar();
 printf("Plaintext: ");fgets(in,sizeof in,stdin);
 for(int i=0;in[i];i++)if(isalpha((unsigned char)in[i])){char c=(char)toupper((unsigned char)in[i]);if(c=='J')c='I';p[n++]=c;}
 p[n]='\0';
 char dig[2000];int d=0;
 for(int i=0;i<n;){char a=p[i++],b='X';if(i<n){if(p[i]==a)b='X';else b=p[i++];} dig[d++]=a;dig[d++]=b;}
 if(d%2)dig[d++]='X'; dig[d]='\0'; makeSquare(key,sq);
 puts("Playfair square:");for(int i=0;i<5;i++){for(int j=0;j<5;j++)printf("%c ",sq[i][j]);puts("");}
 for(int i=0;i<d;i+=2){int r1,c1,r2,c2;pos(sq,dig[i],&r1,&c1);pos(sq,dig[i+1],&r2,&c2);
  if(r1==r2){out[i]=sq[r1][(c1+1)%5];out[i+1]=sq[r2][(c2+1)%5];}
  else if(c1==c2){out[i]=sq[(r1+1)%5][c1];out[i+1]=sq[(r2+1)%5][c2];}
  else {out[i]=sq[r1][c2];out[i+1]=sq[r2][c1];}}
 out[d]='\0';printf("Prepared text: %s\nCiphertext: %s\n",dig,out);return 0;
}
