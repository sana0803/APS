from collections import deque
import sys
# sys.stdin = open("input4.txt")


def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in s[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt

# A가 B를 신뢰한다 / 컴퓨터는 1~N번
# b를 해킹하면 a도 가능
# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 PC 번호 오름차순 출력
# 인접 리스트 / 인접 행렬 메모리 차이

n, m = map(int, input().split())
s = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    s[b].append(a)

result = []
max_cnt = 0

for i in range(1, n + 1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
print(*result)


# N, M = map(int, input().split())
# graph = [[0] * (N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[b][a] = 1
#
# max_cnt = 0
#
# cnt = 0
# for i in range(1, N+1):
#     cnt = bfs(i)
#     if cnt > max_cnt:
#         max_cnt = cnt
#         ans.clear()
#         ans.append(i)
#     elif cnt == max_cnt:
#         ans.append(i)
#
# print(*ans)

