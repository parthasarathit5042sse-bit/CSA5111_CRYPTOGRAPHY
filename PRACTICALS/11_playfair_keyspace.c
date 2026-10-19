#include <stdio.h>
#include <math.h>
int main(void){long double keys=1;for(int i=1;i<=25;i++)keys*=i;printf("Naive ordered 25-letter square key count: 25! = %.0Lf\n",keys);printf("Approximate power of 2: 2^(log2(25!)) where log2(25!) = %.3Lf\n",logl(keys)/logl(2.0L));puts("If keys that produce equivalent Playfair transformations are considered identical, the effective count is smaller; exact counting depends on the equivalence convention used.");return 0;}
