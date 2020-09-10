#include<iostream>
#include<string.h>
 
using namespace std;
 
// A function to find the factorial.
int factorial(int n)
{
	int i;
	for(i = n-1; i > 1; i--)
		n *= i;
 
	return n;
}
 
// A function to calculate the total number of permutation possible for the given set. 
int CountPermutation(char *str)
{
	int countoccur[26] = {0}, len, i, res;
	len = strlen(str);
 
	// Count the occurrence of each character.
	for(i = 0; i < len; i++)
	{
		countoccur[str[i]-'a']++;
	}
 
	res = factorial(len);
 
	// Divide the length factorial by the factorial of number of occurrence of each character.
	for(i = 0; i < 26; i++)
	{
		if(countoccur[i] > 1)
			res = res/factorial(countoccur[i]);
	}
 
	return res;
}
 
int main()
{
	int result;
	char str[100];
	cout<<"A program to find a permutation of a given string: ";
	cout<<"\n\n\tEnter the string: ";
	cin>>str;
 
	// Get result using CountPermutation().
	result = CountPermutation(str);
 
	cout<<"\nThe number of possible permutation are: "<<result;
 
	return 0;
}