from random import randint


def flip(arr, k):
	if k == 0:
		return arr
	assert k <= len(arr), 'k >= len(arr)'
	if arr == []:
		return []
	return [arr[k-1]] + flip(arr[:k-1]+arr[k:], k-1)


def pancake_sort(arr):
	if len(arr) <= 1:
		return arr
	min_i = None
	min_x = None
	for i in range(len(arr)):
		if min_x is None or arr[i] <= min_x:
			min_i, min_x = i, arr[i]
	else:
		arr = flip(arr, min_i+1)
	return [arr[0]]+pancake_sort(arr[1:])
		


if __name__ == '__main__':
	arr = [randint(1, 20) for _ in range(20)]

	print(arr)
	#r = flip(arr,5)
	#print(r)
	r2 = pancake_sort(arr)
	print(r2)
