# 1) Write a function to reverse a given string

def reverse_string(s):
  if s is None:
    return ''
  if len(s) <= 1:
    return s
  return s[-1] + reverse_string(s[:-1])
  

s = 'ciao'
result = reverse_string(s)
print(result)


# 2) Given an unsorted array of unique integers (size n + 1) and a second array that is identical to the first array but missing one integer (size n), find and output the missing integer

from random import randint, shuffle


arr_length = 10
arr1 = [randint(1, 1000) for x in range(arr_length)]
arr2 = arr1+[randint(1, 1000)]
shuffle(arr2)


def partial_sum(arr1, arr2):
  if len(arr1) == 0 or len(arr2) == 0:
    return sum(arr1) - sum(arr2)
  return arr1[0]-arr2[0] + partial_sum(arr1[1:], arr2[1:])


print(arr1)
print(arr2)
print(partial_sum(arr2, arr1))
