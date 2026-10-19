#include <stdio.h>
/* Educational CTR structure with placeholder keystream function; not a standard cipher. */
unsigned char enc_counter(unsigned char ctr){return (unsigned char)(ctr^0x5A);}
int main(void){unsigned char p[]={1,2,4};puts("Educational CTR demonstration (replace enc_counter with a real block cipher):");for(int i=0;i<3;i++)printf("C%d = %02X\n",i+1,(unsigned char)(p[i]^enc_counter((unsigned char)i)));return 0;}
