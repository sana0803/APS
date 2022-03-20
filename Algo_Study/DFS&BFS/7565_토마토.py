import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# arr = [[0 for _ in range(M)] for _ in range(N)]
dr = [0, 0, -1, 1] # 상하좌우
dc = [-1, 1, 0, 0]
# print(DataFrame(box))


def bfs(box, a, b):
    # 처음 a, b에서 시작하는 것이기 때문에 방문체크하고 시작함
    q = [(a, b)]
    visited[a][b] = 1
    cnt = 0

    while q:
        r, c = q.pop(0)  # q의 맨 앞(0) 에서 하나를 뽑는다
        for i in range(4):  # 4방 탐색
            nr = r + dr[i]  # 다음 nr, nc (next_r, next_c 약자)
            nc = c + dc[i]
            # 상자 범위 내이고 / 아직 익지 않은 토마토라면
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # q에 추가하고 방문체크
                q.append((nr, nc))
                visited[nr][nc] = 1
                box[nr][nc] = box[r][c] + 1
                cnt += 1

    print(cnt)


# 익은 토마토 1, 익지않은 토마토 0, 빈칸 -1
M, N = map(int, input().split())    # M이 가로, N이 세로
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:    # 1인 칸만
            bfs(box, i, j)

