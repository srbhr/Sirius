def prefixsum(arr, n, prefix):
	prefixed[0] = arr[0]
	for i in range(1,n):
		prefixed[i] = prefixed[i-1]+arr[i]


arr = [12,23,34,45,56,67,78,89,90]
n=len(arr)
prefixed = [0]*n

prefixsum(arr, n, prefixed)

print("Original Array")

for i in range(n):
	print(arr[i]," ",end="")

print('\n')



for i in range(n):
	print(prefixed[i]," ",end="")

