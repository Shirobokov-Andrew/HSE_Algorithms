import bisect


def fits(people_in_town, l, r, x):
    left = bisect.bisect_left(people_in_town, (x, l))
    right = bisect.bisect_right(people_in_town, (x, r))
    return left < right


n = int(input())
people_in_town = [(int(val), i + 1) for i, val in enumerate(input().split())]
people_in_town.sort(key=lambda x: x[0])
q = int(input())
# answer = ''
for i in range(q):
    query = tuple(map(int, input().split()))
    answer = str(int(fits(people_in_town, query[0], query[1], query[2])))
    print(answer, end='')
