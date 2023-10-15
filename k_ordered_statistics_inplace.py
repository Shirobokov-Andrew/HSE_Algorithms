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
        c = next(gen);
        d = next(gen)
        yield (c << 8) ^ d


def partition(x, start, end):
    mid = start
    pivot = random.choice(x[start:end + 1])
    while mid <= end:
        if x[mid] < pivot:
            x[start], x[mid] = x[mid], x[start]
            start += 1
            mid += 1
        elif x[mid] > pivot:
            x[mid], x[end] = x[end], x[mid]
            end -= 1
        else:
            mid += 1
    return start, mid


def quicksort(x, start, end, q):
    if start >= end:
        return x[start]
    less, greater = partition(x, start, end)
    equal = greater - less
    if q < less:
        return quicksort(x, start, less - 1, q)
    elif q < less + equal:
        return x[q]
    else:
        return quicksort(x, greater, end, q)


n, q = map(int, input().split())
a, b = map(int, input().split())
x = list(itertools.islice(nextRand32(a, b), n))  # данный массив
print(quicksort(x, 0, len(x) - 1, q - 1))
