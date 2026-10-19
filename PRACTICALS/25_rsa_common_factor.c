#include <stdio.h>
long long gcd(long long a,long long b){while(b){long long t=a%b;a=b;b=t;}return a;}
int main(void){long long n,m;printf("Enter RSA modulus n and plaintext block m: ");if(scanf("%lld%lld",&n,&m)!=2)return 1;long long g=gcd(n,m);printf("gcd(m,n) = %lld\n",g);if(g>1&&g<n)printf("Yes: this nontrivial gcd reveals a factor of n, breaking RSA modulus security.\n");else puts("No nontrivial factor found from this block.");return 0;}
