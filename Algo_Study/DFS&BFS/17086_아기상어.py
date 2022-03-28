import sys
sys.stdin = open("input17086.txt")
from collections import deque

dr = [-1, -1, -1, 0, 1, 0, 1, 1]
dc = [-1, 0, 1, 1, 1, -1, 0, -1]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] # 공간 정보 / 1이 아기상어
# 안전 거리 : 그 칸과 가장 가까운 아기 상어와의 거리 / 안전거리 최댓값 구하기
# print(graph)

# 상어 좌표를 모두 큐에 넣어주기
shark = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            shark.append((i, j))

# 상어 위치부터 BFS 탐색. 8방 탐색하여 0이면 1씩 더하면서 거리 세기
def bfs():
    while shark:
        r, c = shark.popleft()     # 큐의 맨 앞(0) 에서 하나를 뽑는다

        for k in range(8):     # 8방 탐색
            nr = r + dr[k]     # 다음 nr, nc (next_r, next_c 약자)
            nc = c + dc[k]
            # 격자 범위 내이면
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0:  # 칸 값이 0이면 1씩 더하면서 거리 세기
                    # 큐에 추가하고 1 더하기
                    shark.append((nr, nc))
                    graph[nr][nc] = graph[r][c] + 1
    return


bfs()
safe = 0    # 처음 안전거리
for i in range(N):
    for j in range(M):
        safe = max(safe, graph[i][j])   # 최대거리 갱신

print(safe - 1)