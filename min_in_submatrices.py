n, L = [int(i) for i in input().split()]
matrix = [[0] * n for i in range(n)]
for i in range(n):
    matrix[i][::] = [int(i) for i in input().split()]
for i in range(n):
    for j in range(n - L + 1):
        matrix[i][j] = min(matrix[i][j:j + L])
for j in range(n):
    for i in range(n - L + 1):
        matrix[i][j] = min([matrix[k][j] for k in range(i, i+L)])
for i in range(n - L + 1):
    for j in range(n - L + 1):
        print(matrix[i][j], end=' ')
    print()
