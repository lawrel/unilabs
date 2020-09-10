#include <stdio.h>
#include <math.h>
int fibIterative(int n) {
  int f[n+2];
  f[0] =0;
  f[1] =1;
  for (int i = 2; i < n; i++) {
    f[i] = f[i-1] + f[i-2];
  }
  return f[n];
}
int fibRecurse(int n) {
  if (n<=1) {
    return n;
  } else {
    return fibRecurse(n-1) + fibRecurse(n-2);
  }
}
int fibDirect(int n) {
  return round(pow(((1+sqrt(5))/2),n)/sqrt(5));
}
