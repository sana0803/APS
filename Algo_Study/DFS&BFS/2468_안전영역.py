import sys
sys.stdin = open("input3.txt")
from pandas import DataFrame

dr = [0, 0, -1, 1] # 상하좌우
dc = [-1, 1, 0, 0]


def bfs(a, b, height):
    # 처음 a, b에서 시작하는 것이기 때문에 방문체크하고 시작함
    q = [(a, b)]
    visited[a][b] = 1    # 방문체크

    while q:
        r, c = q.pop(0)     # q의 맨 앞(0) 에서 하나를 뽑는다

        for k in range(4):     # 4방 탐색
            nr = r + dr[k]     # 다음 nr, nc (next_r, next_c 약자)
            nc = c + dc[k]
            # 격자 범위 내이고 / 최저높이보다 높으면서 아직 방문 안했을때
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] > height and not visited[nr][nc]:
                    # q에 추가하고 방문체크
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    return


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)] # 높이 정보
# 안전 영역 : 상하좌우 인접해있으며 크기가 최대인 영역
# print(graph)
min_height = min(map(min, graph))   # 최저 높이
max_height = max(map(max, graph))   # 최고 높이

ans = 1
for height in range(min_height, max_height+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and visited[i][j] == 0: # 아직 방문 안했고 최저높이보단 높으면
                bfs(i, j, height)
                cnt += 1    # 갯수세기

    ans = max(ans, cnt) # 더 많은거로 답 갱신

print(ans)

