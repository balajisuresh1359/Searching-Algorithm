def binarySearch(array,start,end,key):
	while start <=end :
		mid = (start+end)//2
		if array[mid] == key:
			return mid
		elif array[mid] > key:
			end=mid-1
		else:
			start=mid+1
	return -1
def jumpSearch(array,key,jumplength):
	i=0
	size=len(array) 
	while i < size:
		i=i+jumplength
		if i<size and array[i] >= key:
			return binarySearch(array,i-jumplength,i,key)
	return -1



array=[x for x in range(1,1000)]
print(jumpSearch(array,78,50))
