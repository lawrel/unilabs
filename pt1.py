import sys
import timeit
import functools
import random

def randNdig(n):
	start = 10**(n-1)
	end = (10**n)-1
	return random.randint(start,end)

def method1(x,y):
	index = 0
	answer = 0
	while y:
		if (y%2==1):
			answer += x<<index
		++index
		y>>=1
	return answer

def method2(x,y):
	if (y==0):
		return 0
	z = method2(x,(y>>1))
	if (y%2==0):
		return (z<<1)
	else:
		return x + (y<<1)

def method3(x,y):
	n = max(x.bit_length(),y.bit_length())
	if n<=1:
		return x*y
	lhalf = n>>1
	rhalf = (1<<lhalf)-1
	xleft = x>>lhalf
	xright = x&rhalf
	yleft = y>>lhalf
	yright = y&rhalf
	P1 = method3(xleft,yleft)
	P2 = method3(xright,xleft)
	P3 = method3((xright+xleft),(yright+yleft))
	return (((P1<<lhalf)+(P3-P1-P2))<<lhalf)+P2

d = int(sys.argv[1])
x = randNdig(d)
y = randNdig(d)
print("Method 1:")
time = timeit.Timer(functools.partial(method1,x,y))
print(time.timeit(1))
time = timeit.Timer(functools.partial(method2,x,y))
print("Method 2: ")
print(time.timeit(1))
print("Method 3: ")
time = timeit.Timer(functools.partial(method3,x,y))
print(time.timeit(1))