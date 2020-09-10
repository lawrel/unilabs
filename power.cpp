#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int power3(int n) {
	if(n==0) {return 1;}
	else {
		return 3*power3(n-1);
	}
}
int power2(int n) {
	if(n==0) {return 1;}
	else {
		return 2*power2(n-1);
	}
}

int main() {
	int input;
	cin>>input;
	while (input!=0) {
		cout<<power3(power2(input)<<endl;
		cin>>input;
	}
	return 0;
}