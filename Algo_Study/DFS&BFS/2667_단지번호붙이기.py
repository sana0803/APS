import sys
sys.stdin = open("input.txt")
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque() # dequeue
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:    # queue가 비기전까지
        x, y = queue.popleft()  # 시간복잡도 o(1) 좀더 빠른애
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:  # 1인 곳을 0으로 바꿔
                graph[nx][ny] = 0   # 다시 방문하지 않도록 하기(방문체크)
                queue.append((nx, ny))
                count += 1      # 집의 개수 세기
    return count


n = int(input())    # 지도 크기
graph = []
for i in range(n):  # 지도 만들기
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:    # 1인 칸만 숫자 세서 cnt에 추가
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))     # len으로 단지가 몇개인지 출력
for i in range(len(cnt)):
    print(cnt[i])