# Given a list of points as [x,y] pairs; a vertex in [x,y] form; and an integer k, return the kth closest points in terms of euclidean distance

from random import random, randint
from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', ['x', 'y'])

def rand(max):
    return round(random()*max, 2)

def distance(p1, p2):
    if all([isinstance(p1, Point), isinstance(p2, Point)]) is False:
            print("Input type error. Both arguments must be of Point type")
    return sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)


def k_closest(v, arr, k):
    if len(arr) <= k:
        return arr
    if len(arr) == 0 or k == 0:
        return []
    p0 = arr[0]
    closer = [p for p in arr[1:] if distance(p, v) <= distance(p0, v)]
    further = [p for p in arr[1:] if distance(p, v) > distance(p0, v)]

    if len(closer) > k:
        return k_closest(v, closer, k)
    elif len(closer) == k-1:
        return closer + [p0]
    elif len(closer) == k:
        return closer
    elif len(closer) < k:
        return [p0] + closer + k_closest(v, further, k-len(closer)-1)
    else:
        assert False, 'Should not enter in this branch'


if __name__ == '__main__':

    # Generate points
    arr = [Point(rand(10), rand(10)) for _ in range(10)]
    v = Point(rand(10), rand(10))
    k = randint(2, 8)
    print("Vertex:"+str(v.x)+','+str(v.y))
    arr_dist = [(p, round(distance(p, v),2)) for p in arr]
    print("arr", *arr_dist, sep='\n')
    print("k:", k)

    closest = k_closest(v, arr, k)
    closest_dist = [(p, round(distance(p, v),2)) for p in closest]

    print(*closest_dist, sep="\n")
