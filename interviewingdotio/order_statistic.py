
# Given a Set of numbers, find and return the 3rd smallest number

from random import sample, randint, shuffle
from time import time
from matplotlib import pyplot as plt
import numpy as np


class Counter(object) :

	def __init__(self, fun) :
		self._fun = fun
		self.counter=0
	
	def __call__(self,*args, **kwargs) :
		self.counter += 1
		return self._fun(*args, **kwargs)


class CallCounter(object) :

	def __init__(self, fun, iterations, sizes):
		self._fun = fun
		self.iterations=iterations
		self.sizes=sizes
		self.avg_count = {}
		self.times = {}
	def get_avg_calls(self):
		for size in self.sizes:
			self._fun.counter = 0
			l = list(set(randint(1, 500000) for i in range(size)))
			shuffle(l)
			
			start = time()
			for i in range(self.iterations):
				r = self._fun(l, int(len(l)/3))
			self.times[size] = (time()-start)/self.iterations
			self.avg_count[size] = self._fun.counter/self.iterations


def find_nth_smallest(data, n):
	if n > len(data):
		return None
	x0 = data[0]
	smaller = [x for x in data if x < x0]
	larger = [x for x in data if x > x0]
	if len(smaller) > n-1:
		return find_nth_smallest(smaller, n)
	elif len(smaller) == n-1:
		return x0
	elif len(smaller) < n-1:
		return find_nth_smallest(larger, n-len(smaller)-1)


find_nth_smallest = Counter(find_nth_smallest) 
call_counter = CallCounter(find_nth_smallest, iterations=50, sizes=range(500, 100000, 500))

call_counter.get_avg_calls()

figure0 = plt.figure()
plt.scatter(list(call_counter.avg_count.keys()), list(call_counter.avg_count.values()))
plt.scatter(list(call_counter.avg_count.keys()), 2*np.log(list(call_counter.avg_count.keys())))
plt.show()

# figure = plt.figure()
# plt.scatter(list(call_counter.times.keys()), list(call_counter.times.values()))
# plt.plot(list(call_counter.times.keys()), np.log(list(call_counter.times.keys())))
# plt.show()


