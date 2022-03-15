import sys
sys.stdin = open("input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(a, b):
    q = [(a, b)]
    graph[a][b] = 1

    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not graph[nr][nc]:
                q.append((nr, nc))
                graph[nr][nc] = 1


# 가로 세로 구분 잘 하기
while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        graph = [[0] * N for _ in range(N)]