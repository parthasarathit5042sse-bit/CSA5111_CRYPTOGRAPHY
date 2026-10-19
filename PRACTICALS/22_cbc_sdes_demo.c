#include <stdio.h>
#include <string.h>
/* Educational CBC XOR chaining demo with a placeholder block transform. Not standard S-DES. */
void block(unsigned char in,unsigned char *out){*out=(unsigned char)(in^0xA5);}
int main(void){unsigned char p[]={0x01,0x23},iv=0xAA,prev=iv,c[2];puts("Educational CBC chaining demonstration (placeholder block transform, not standard S-DES):");for(int i=0;i<2;i++){unsigned char x=p[i]^prev;block(x,&c[i]);prev=c[i];printf("C%d = %02X\n",i+1,c[i]);}return 0;}
