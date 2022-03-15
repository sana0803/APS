import sys
import copy
from collections import deque
sys.stdin = open("input3.txt")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ans = 0
q = deque()


def bfs():
    global ans
    w = copy.deepcopy(arr)

    # 바이러스를 모두 몰아주기 위해 큐에 모든 바이러스 넣어주기
    for i in range(N):
        for j in range(M):
            if w[i][j] == 2:
                q.append([i, j])

    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 바이러스가 퍼질 수 있고, 한번도 바이러스가 방문하지 않은 곳이면 큐에 넣기
            if 0 <= nr < N and 0 <= nc < M:
                if w[nr][nc] == 0:
                    w[nr][nc] = 2
                    q.append([nr, nc])

    # 바이러스 다 퍼진 다음에 안전영역 카운트하기
    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)


# 3개의 벽을 세우는 모든 경우의 수 찾기
def wall(x):
    if x == 3:  # 탈출조건
        bfs()
        return

    for i in range(N):
        for j in range(M):
            # 일반 구역이라면 벽을 세워서 다음으로 넘김
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x + 1)
                # 재귀가 끝나면 최대로 3개의 벽을 세울수 있어서 다른곳도 세워보기 위해서 벽 없앰
                arr[i][j] = 0


wall(0)
print(ans)