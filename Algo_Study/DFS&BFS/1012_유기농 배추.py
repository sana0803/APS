import sys
sys.stdin = open("input2.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(a, b):
    q = [(a, b)]
    visited[a][b] = 0

    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 1:
                visited[nr][nc] = 0
                q.append((nr, nc))
    return


T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    # M 배추밭 가로길이 / N 배추밭 세로길이 / K 배추 심어져있는 위치 개수
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    # 인접 행렬로 배추 위치 찾기
    for _ in range(K):
        a, b = map(int, input().split())
        visited[a][b] = 1  # 배추 위치 표시

    for r in range(N):
        for c in range(M):
            if visited[r][c] == 1:
                bfs(r, c)
                visited[r][c] = 0
                cnt += 1
    print(cnt)


# print(visited)