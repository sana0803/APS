import sys
sys.stdin = open("input2.txt")

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            res += 1

print(res)