#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;
int main() {
    int A, B, C = 0;
    cin >> A >> B;
    for (int i = A; i <= B; i++) {
        if (i > 1) {
            bool isPrime = true;
            for (int j = 2; j * j <= i; j++) { 
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                printf("%d ", i);
                C++;
            }
        }
    }
    printf("\nTotal primes: %d", C);
}
