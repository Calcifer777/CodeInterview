from random import randint


def get_different_number(arr):

	for i, x in enumerate(arr):
		if x < len(arr) and x != i:
			arr[x] = x

	for i, x in enumerate(arr):
		if x != i:
			return i

	return len(arr)+1


if __name__ == '__main__':
	
	arr = list(set(randint(0, 30) for _ in range(60)))

	print(arr)

	print(get_different_number(arr))

