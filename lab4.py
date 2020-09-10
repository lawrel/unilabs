import sys
import random 

def Rselect(x,k):
	if k == 0: return "Invalid K"
	def select(array,s,e,k):
		if e==s: return array[s]
		else:
			pivot = random.randint(s,e)
			array[s],array[pivot] = array[pivot],array[s]
			index = s
			for j in range(s+1,e+1):
				if array[j] < array[s]:
					index += 1
					array[index], array[j] = array[j], array[index]
			array[s],array[index] = array[index],array[s]
			if index == k:
				return array[index]
			elif index > k:
				return select(array,s,index-1,k)
			else:
				return select(array,index+1,e,k)
	return select(x,0,len(x)-1,k-1)

n = int(sys.argv[1])
k = int(sys.argv[2])
x = []
for i in range(0,n):
	x.append(random.randint(0,n-1))
print("Selected:",Rselect(x,k))
print("Array:",x)
x.sort()
print("Sorted Array:",x)