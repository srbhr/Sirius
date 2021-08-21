from sys import stdin, stdout


def isPresent(arr,num, i):
	if arr[i]==num:
		return i
	if i==len(arr)-1:
		return False
	return (isPresent(arr,num,i+1))


arr = [12,23,43,45,56,67,87,89,10]
num =  10
print(isPresent(arr,num,0))

