import sys
sys.stdin = open("input2.txt")
from pandas import DataFrame

dr = [0, 0, -1, 1] # 상하좌우
dc = [-1, 1, 0, 0]
# arr = [[0 for _ in range(M)] for _ in range(N)]


def bfs(graph, a, b):
    # 처음 a, b에서 시작하는 것이기 때문에 방문체크하고 시작함
    q = [(a, b)]
    graph[a][b] = -1    # 방문체크
    cnt = 1

    while q:
        r, c = q.pop(0)     # q의 맨 앞(0) 에서 하나를 뽑는다

        for k in range(4):     # 4방 탐색
            nr = r + dr[k]     # 다음 nr, nc (next_r, next_c 약자)
            nc = c + dc[k]
            # 격자 범위 내이고 / 주위에 쓰레기가 있으면
            if 0 < nr <= N and 0 < nc <= M and graph[nr][nc] == 1:  # 범위 잘 보기
                # q에 추가하고 방문체크
                q.append((nr, nc))
                graph[nr][nc] = -1
                cnt += 1    # 쓰레기 크기 세기

    return cnt


N, M, K = map(int, input().split())    # M이 가로, N이 세로, k는 쓰레기 개수

graph = [[0] * (M+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1  # 쓰레기 위치 표시

# print(DataFrame(graph))
count = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1:    # 1인 칸만 숫자 세서 count에 추가
            count.append(bfs(graph, i, j))
        # print(count)

print(max(count))