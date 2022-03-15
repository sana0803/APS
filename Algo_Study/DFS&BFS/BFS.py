N = 6

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]


# N x N 격자 (a, b) 에서 bfs 탐색 시작
def bfs(a, b):
    # 처음 a, b에서 시작하는 것이기 때문에 방문체크하고 시작함
    q = [(a, b)]
    visited[a][b] = 1
    while q:
        r, c = q.pop(0)        # q의 맨 앞(0) 에서 하나를 뽑는다 / dfs는 그냥 pop()만 바꾸면 됨
        for i in range(4):     # 4방 탐색
            nr = r + dr[i]     # 다음 nr, nc (next_r, next_c 약자)
            nc = c + dc[i]
            # 격자 범위 내이고 / 아직 방문하지 않았으면
            # 문제에 따라 여기 조건이 추가될 수 있음. (ex. 그래프가 연결되어 있을 때만 방문)
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # q에 추가하고 방문체크
                q.append((nr, nc))
                visited[nr][nc] = 1

