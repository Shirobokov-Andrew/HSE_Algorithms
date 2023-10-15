import itertools
import random


def nextRand24(a, b):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield cur >> 8


def nextRand32(a, b):
    gen = nextRand24(a, b)
    while True:
        c = next(gen); d = next(gen)
        yield (c << 8) ^ d


def quicksort(x, q):
    if len(x) == 1:
        return x[0]
    pivot = random.choice(x)
    less = []
    equal = []
    greater = []
    for i in x:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    l = len(less)
    e = len(equal)
    if q < l:
        return quicksort(less, q)
    elif q < l + e:
        return equal[q - l]
    else:
        return quicksort(greater, q - l - e)


def quicksort_inplace(x, l, r):
    if l <= r:
        return



n, q = map(int, input().split())
a, b = map(int, input().split())
x = list(itertools.islice(nextRand32(a, b), n)) # данный массив
print(quicksort(x, q - 1))
