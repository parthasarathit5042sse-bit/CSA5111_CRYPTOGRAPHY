#include <stdio.h>
int main(void){puts("DES key schedule demonstration");puts("After PC-1, DES has two disjoint 28-bit halves C and D.");puts("Each round rotates both halves, then PC-2 selects 24 bits from C and 24 bits from D.");puts("Thus each 48-bit subkey contains 24 bits from each half. The exact subsets are defined by the DES PC-2 table.");return 0;}
