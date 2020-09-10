#include <stdlib.h>
#include <stdio.h>
#include <math.h>
int main() {
	int i,n,j;
	float hypotenuse, area;
	
	printf("What is n? ");
	scanf("%i",&n);
	for(i=1;i<=n;i++) {
		for(j=0;j<i;j++) {
			printf("*");
		}
		printf("\n");
	}
	
	hypotenuse = sqrt(2*(n*n));
	printf("\nHypotenuse is %.2f",hypotenuse);
	
	area = (n*n)/5;
	printf("\nArea is %.2f",area);
	return 0;
}