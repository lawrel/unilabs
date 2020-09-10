#include <stdio.h>

/* 
   Use d0, d1, and carry_in to compute a return value.
   If necessary, use the carry_out pointer to return additional information
*/
int add_two_bits(int d0, int d1, int carry_in, int *carry_out)
{
  int xor = d0 ^ d1;
  int s = carry_in ^ xor;
  if (carry_out) {
    *carry_out = (carry_in & xor) | (d0 & d1);
  }
    return s;
}
void printarr(int *x) {
  int i;
  for(i=0;i<4;i++) {
    printf("%d",x[i]);
  }

}
int main()
{
  int i,cout;
  int d0[4];
  int d1[4];
  int ci[4];
  int sum[4];

  for(i=0;i<4;i++) {
    printf("Enter binary digit d0[%d]: ",i);
    scanf("%d", &d0[i]);
    d0[i] = !!d0[i];
  }
  for(i=0;i<4;i++) {
    printf("Enter binary digit d1[%d]: ",i);
    scanf("%d", &d1[i]);
    d1[i] = !!d1[i];
  }
  /* Call add_two_bits multiple times */
  ci[0] = 0;
  for (i=3;i>=0;i--) {
    sum[i] = add_two_bits(d0[i],d1[i],ci[i],&cout);
    if (i!=0) {
      ci[i-1] = cout;
    }
  }
  if (cout==1) {
    printarr(d0); printf(" + ");
    printarr(d1); printf(" = ");
    printarr(sum);
    printf(" with a carry\n");
  }
  else {
    printarr(d0); printf(" + ");
    printarr(d1); printf(" = ");
    printarr(sum);
    printf(" without a carry\n");
  }

  return 0;
}
