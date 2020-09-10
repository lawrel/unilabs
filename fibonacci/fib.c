#include <stdio.h>
#include <stdlib.h>
int* results;
int memFib(int n) {
	if (n == 0) {
		return 0;
	} else if (n <= 2) { 
		return 1;
	}
	if (results[n] != 0) {
		return results[n];
  } else {
		results[n] =  memFib(n - 1) + memFib(n - 2);
		return results[n];
  }
}
int Fib(int n) {
	if (n == 0) {
		return 0;
	} else if (n <= 2) { 
		return 1;
	} else {
		return memFib(n - 1) + memFib(n - 2);
  }
}
int main(int argc, char **argv) {
	int n,i;
	if (argc!=3){
		return -1;
	}
	n = atoi(argv[1]);
	results = (int*)calloc(n,sizeof(int));
	for (i=0;i<=n;i++) {
		results[i] = 0;
	}
	if (atoi(argv[2])!=0){
		printf("%d",memFib(n));
	} else {
		printf("%d",Fib(n));
	}
	return 0;
}
