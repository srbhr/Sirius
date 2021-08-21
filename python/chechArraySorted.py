def isSorted(arr):
	if len(arr)== 0 or len(arr)==1:
		return True
	return arr[0]<arr[1] and isSorted(arr[1:])

arr=[1,2,3,4,5,6,7,8,10]
print(isSorted(arr))
