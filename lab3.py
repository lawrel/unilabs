import sys
import random

carmichael = [561,1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841,
 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 
 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 
 334153, 340561, 399001, 410041, 449065, 488881]

def modexp(x,y,n):
	if y==0: 
		return 1
	z = modexp(x,(y>>1),n)
	if (y%2==0):
		return (z**2)%n
	else:
		return x*(z**2)%n

def primality(n,k):
	if n==1: return "Prime"
	count = 0
	for i in range(0,k):
		a = random.randint(1,n-1)
		if (modexp(a,n-1,n)!=1):
			count+=1
			#return "Not Prime"
	print("For",n,count,"tests failed")
	if (count==0):
		return "Prime"
	else: return "Not Prime"
	
	

x = int(sys.argv[1])
if (x==0):
	for i in range(0,len(carmichael)):
		print(carmichael[i]," is ",primality(carmichael[i],1000))
else:
	print(x," is ",primality(x,1000))