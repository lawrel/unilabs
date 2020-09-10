#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0) {
       return a; 
    } else {
       return gcd(b, a%b);
	}
}
int main()
{
    int a = 10, b = 15;
    printf("GCD(%d, %d) = %d", a, b, gcd(a, b));
    a = 35, b = 10;
    printf("\nGCD(%d, %d) = %d", a, b, gcd(a, b));
    a = 31, b = 2;
    printf("\nGCD(%d, %d) = %d", a, b, gcd(a, b));
    return 0;
}