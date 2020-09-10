import sys
import timeit
import functools

def fib1(n):
	if n==0: return 0
	elif n==1: return 1
	else: return fib1(n-1)+fib1(n-2)

n = sys.argv[1]
time = timeit.Timer(functools.partial(fib1,n))
print(time.timeit(1))