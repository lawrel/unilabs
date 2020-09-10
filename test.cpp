#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
int n = 0;
for (unsigned int i =999; i<999999; i++) {
	int s = 0;
	int a = i;
	while (a>0) {
		s += a%10;
		a = a/10;
	}
	if (s==27) {
		n++;
	}
}
cout<<n;
}