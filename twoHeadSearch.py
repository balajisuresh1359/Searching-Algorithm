def twoHeadsearch(array,n):
	left=0
	right=len(array)-1
	while left<=right:
		if array[left] == n or array[right] == n:
			return left
		left+=1
		right-=1
	return -1


array=[x for x in range(1,1000)]
print(twoHeadsearch(array,10))
