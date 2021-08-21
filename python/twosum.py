def twoSum(sum, arr):
	s = set()
	for i in range(len(arr)):
		target = sum-arr[i]
		if(target in s):
			print(arr[i], target)
		s.add(arr[i])


arr = [1,2,2,5,6]
sum = 6

twoSum(sum,arr)
