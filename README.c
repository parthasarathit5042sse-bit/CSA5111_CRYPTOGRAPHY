
#include <stdio.h>

int main() {
    int p, q, n, phi, e, m;
    int d = 1, c, decrypted;

    printf("Enter p: ");
    scanf("%d", &p);

    printf("Enter q: ");
    scanf("%d", &q);

    printf("Enter message: ");
    scanf("%d", &m);

    printf("Enter public exponent e: ");
    scanf("%d", &e);

    n = p * q;
    phi = (p - 1) * (q - 1);

    printf("\nn = %d", n);
    printf("\nPhi(n) = %d", phi);

    // Check whether e is valid
    int a = e, b = phi;

    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }

    if (a != 1 || e <= 1 || e >= phi) {
        printf("\nInvalid public exponent e");
        return 0;
    }

    // Find private key d
    while ((d * e) % phi != 1) {
        d++;
    }

    // RSA encryption
    c = 1;
    for (int i = 0; i < e; i++) {
        c = (c * m) % n;
    }

    // RSA decryption
    decrypted = 1;
    for (int i = 0; i < d; i++) {
        decrypted = (decrypted * c) % n;
    }

    printf("\nPublic key: (%d, %d)", e, n);
    printf("\nPrivate key: (%d, %d)", d, n);
    printf("\nEncrypted message: %d", c);
    printf("\nDecrypted message: %d\n", decrypted);

    return 0;
}
