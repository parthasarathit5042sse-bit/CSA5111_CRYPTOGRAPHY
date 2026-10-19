#include <stdio.h>
int main(void){puts("CBC mode comparison: 3DES vs DES");puts("Security: choose 3DES over DES if constrained to these two; DES has a 56-bit key and is obsolete.");puts("Performance: DES is faster than 3DES, but neither is recommended for new systems.");puts("For real applications, prefer a modern authenticated cipher such as AES-GCM or ChaCha20-Poly1305.");return 0;}
