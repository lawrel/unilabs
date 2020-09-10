import sys
import timeit
import functools

def fib2(n):
	if n==0: return 0
	elif n==1: return 1
	else:
		n0 = 0
		n1 = 1
		n2 = 0
		for i in range(2,n+1):
			n2 = n0+n1
			n0 = n1
			n1 = n2
		return n2

#n = int(sys.argv[1])
n = 2**19
time = timeit.Timer(functools.partial(fib2,n))
print(time.timeit(1))
#print(fib2(n))
