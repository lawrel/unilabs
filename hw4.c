#include <stdio.h>
#include <math.h>
int sb[64] = {0}; 

void parallelblock(int a,int b,int *p, int *g) {
	*g = (a & b);
	*p = (a ^ b);
}
void serialblock(int c0,int *p,int *g,int *gg,int *gp,int *c4, int i) {
	//calculate group propogate and group generate
	int x = (p[0] & p[1]); 
	int y = (p[2] & g[3]);
	*gg = (g[0] | ((g[1] & p[0])|((x & g[2])|(x & y))));
	*gp = x & (p[3] & p[2]);
	//calculate all the carry ins
	int w = (p[0] & c0); 
	int z = (p[1] & p[2]);
	int c1 = (w | g[0]);
	int c2 = ((p[1] & g[0]) | g[1]) | (p[1] & w);
	int c3 = (((z & w) | (z & g[0])) | (p[2] & g[1])) | g[2];
	//calculate all the sum bits and add them to sum array
	int s0 = (p[0] ^ c0);
	int s1 = (p[1] ^ c1);
	int s2 = (p[2] ^ c2);
	int s3 = (p[3] ^ c3);
	*c4 = g[3] | (p[3] & c3);
	sb[i-1] = s3;
	sb[i-2] = s2;
	sb[i-3] = s1;
	sb[i-4] = s0;
}
int four (int *a,int *b,int cin) {
	int p[4] = {0};
	int g[4] = {0};
	int pg[4] = {0};
	int gg[4] = {0};
	int i; int cout = 0;
	for(i=0;i<4;i++) {
		parallelblock(a[i],b[i],&p[i],&g[i]);
	}
	serialblock(cin,p,g,&gg[0],&pg[0],&cout,i);
	return cout;
}
int add (int *a,int *b,int cin) {
	int p[4] = {0}; int z=0;
	int g[4] = {0}; int j;
	int pg[4] = {0};
	int gg[4] = {0}; int k;
	int i;

	for (k=0;k<4;k++) {
		for (j=0;j<4;j++) {
			for(i=0;i<4;i++) {
				parallelblock(a[z],b[z],&p[i],&g[i]);
				z++;
			}
			serialblock(cin,p,g,&gg[j],&pg[j],&cin,z);
		}
	}
	return cin;
}
long bintodec(int *x) {
	int i;
	long t = 0;
	for(i=0;i<64;i++) {
		if (x[i]==1) {
			long temp = pow(2,i);
			t = t+temp;
		}
	}
	return t;
}
void printarr(int *x) {
  int i;
  for(i=64;i>0;i--) {
    printf("%d",x[i-1]);
  }
}
int main() {
	long a=0; long b=0;
	int ab[64] = {0};
	int bb[64] = {0};
	int st;
	
  	printf("Enter A (hex): \n");
  	scanf("%lx",&a);
	printf("Enter B (hex): \n");
	scanf("%lx",&b);
	printf("Add (0) or subtract (1): \n");
	scanf("%d",&st);
	printf("\nA is %016lx or %ld",a,a);
	printf("\nB is %016lx or %ld",b,b);
	if (st==1) {printf("\nInverting %ld", b);}
  	for (int i = 0;i<64;++i){ //store hex into array as binanry
			bb[i] = b&1;
			b >>=1;
		}
	for (int i = 0;i<64;++i){ //store hex into array as binanry
		ab[i] = a&1;
		a >>=1;
	}
	
	if (st == 1) {
		int i;
		for (i=0;i<64;i++) {
			if (bb[i]==1) {
				bb[i] = 0;
			} else {
				bb[i] = 1;
			}
		}
		//int cin = 1;
		printf("\nB (bin) : ");
		printarr(bb);
	} else {
		//int cin = 0;
	}
	long sum = bintodec(sb);
	printf("\n\nCalculate sum, S:");
	printf("\n\nA (bin) : ");
	printarr(ab);
	printf("\nB (bin) : ");
	printarr(bb);
	printf("\nS (bin) : ");
	printarr(sb);
	printf("\n\nS is %016lx or %ld",sum,sum);
  	return 0;
 }