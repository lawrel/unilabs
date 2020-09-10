#include <stdlib.h>
#include <stdio.h>
#include <math.h>

long factorial(long n) {
	long temp;
	if(n<=1) {return 1;}
	temp = n*factorial(n-1);
	return temp;
}

int main() {
	long n,m;
	printf("Enter a number: ");
	scanf("%ld",&n);
	m = factorial(n);
	printf("/nFactorial %ld is %ld",n,m);
	return 0;
}