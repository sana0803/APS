N = 5

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]


def bfs(a, b):
    q = [(a, b)]
    visited[a][b] = 1

    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1


print(visited)

