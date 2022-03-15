from collections import deque
from pandas import DataFrame

import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue

            if arr[nr][nc] == 0:
                continue

            if arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc))

    return arr[n-1][m-1]


print(bfs(0, 0))
# print(DataFrame(arr))