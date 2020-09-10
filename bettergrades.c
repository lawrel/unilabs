#include <stdio.h>
#include <stdlib.h>
struct student {
	char name[100]; // No one should have a name longer than this
	int *grades; // This is the pointer to hold the (integer) grades
	int count; // The number of grades
	};
int main () {
	int n,i,j;
	float avg;
	struct student* students;
	
	printf("How many students are there? ");
	scanf("%d",&n); printf("\n");
	students = (struct student *)malloc(n * sizeof(struct student));
	for(j=0;j<n;j++) {
		printf("Enter the name of student %d: ",j);
		scanf("%s",students[j].name);
		printf("How many grades does %s have? ",students[j].name);
		scanf("%d",&students[j].count);
		if (students[j].count==0) {break;}
		
		students[j].grades = (int *)malloc(n * sizeof(int));
		for (i=0;i<students[j].count;i++) {
			printf("Enter the next grade: ");
			scanf("%d",&students[j].grades[i]);
		}
		printf("\n");
	}
	for(j=0;j<n;j++) {
		avg=0;
		for (i=0;i<students[j].count;i++) {
			avg+=students[j].grades[i];
		}
		avg = avg/students[j].count;
		printf("\n%s has an average grade of %.2f",students[j].name,avg);
	}
	return 0;
}