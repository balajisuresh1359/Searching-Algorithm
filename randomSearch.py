import random
def randomSearch(array,n):
	i=0
	size=len(array)-1
	while i<= size :
		r=random.randint(0,size)
		if array[r] == n:
			pos=array.index(n)
			return pos
		i+=1
	return -1

array=[x for x in range(20,100)]
print(randomSearch(array,34))
