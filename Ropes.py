def smaller(rope_len, K, lengths):
    counter = sum(length // rope_len for length in lengths)
    if counter < K:
        return True
    else:
        return False


N, K = (map(int, input().split()))
lengths = [int(input()) for i in range(N)]
min_length = 0
max_length = 10000000000
while max_length - min_length > 1:
    rope_len = (max_length + min_length) // 2
    if smaller(rope_len, K, lengths):
        max_length = rope_len
    else:
        min_length = rope_len
print(min_length)
