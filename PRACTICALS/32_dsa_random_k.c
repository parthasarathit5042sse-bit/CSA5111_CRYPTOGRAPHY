#include <stdio.h>
int main(void){puts("DSA signatures use a fresh secret nonce k for each signature.");puts("For the same message, different valid k values usually produce different signatures. RSA signatures may also be randomized or deterministic depending on the scheme (e.g. PSS vs PKCS#1 v1.5).");puts("Never reuse DSA/ECDSA nonce k: reuse can reveal the private signing key.");return 0;}
