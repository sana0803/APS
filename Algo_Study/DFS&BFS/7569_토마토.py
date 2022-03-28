import sys
sys.stdin = open("input7569.txt")
from collections import deque

dr = [-1, 1, 0, 0, 0, 0]    # 인접 위치 상하좌우앞뒤
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

# 토마토가 모두 익을때까지 최소 며칠? 모두 익어있으면 0 / 못하면 -1


def bfs(start):
    # 처음 a, b에서 시작하는 것이기 때문에 방문체크하고 시작함
    # visited[a][b] = 1
    cnt = 0

    while tomato:
        h, r, c = tomato.pop(0)  # q의 맨 앞(0) 에서 하나를 뽑는다
        for i in range(4):  # 4방 탐색
            nr = r + dr[i]  # 다음 nr, nc (next_r, next_c 약자)
            nc = c + dc[i]
            nh = h + dh[i]

            # 상자 범위 내이고 / 아직 익지 않은 토마토라면
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # q에 추가하고 방문체크
                tomato.append((nr, nc))
                visited[nr][nc] = 1
                box[nr][nc] = box[r][c] + 1
                cnt += 1

    print(cnt)


# 익은 토마토 1, 익지않은 토마토 0, 빈칸 -1
M, N, H = map(int, input().split())    # M이 가로, N이 세로, H가 높이
box = []
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

tomato = deque()
for i in range(H):
    box.append([list(map(int, input().split())) for _ in range(N)])
    for j in range(N):
        for k in range(M):  # 높이, r, c 순서
            if box[i][j][k] == 1:    # 1인 칸만
                tomato.append((i, j, k))  # 토마토 위치 큐에 넣어주기

print(box)
bfs(tomato)