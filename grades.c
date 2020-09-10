#include <stdio.h>
#include <stdlib.h>
int main() {
	int n,i;
	float avg=0;
	int* grades;
	
	printf("How many grades does the student have? ");
	scanf("%d",&n);
	if(n==0) {return 1;}
	grades = (int *)malloc(n * sizeof(int));
	for (i=0;i<n;i++) {
		printf("Enter the next grade: ");
		scanf("%d",&grades[i]);
	}
	for (i=0;i<n;i++) {
		avg+=grades[i];
	}
	avg = avg/n;
	printf("The average grade is %.2f",avg);
	return 0;
}