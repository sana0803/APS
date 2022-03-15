from collections import deque
import sys
sys.stdin = open("input.txt")

N, M, V = map(int, input().split())
# N 정점의 개수 / M 간선의 개수 / V 탐색을 시작할 정점 번호

graph = [[0] * (N+1) for _ in range(N+1)]

# 인접 행렬로 연결된 노드 찾기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 # 연결 표시
# print(graph)


def bfs(a):
    # 현재 노드 방문처리
    visited = [a]
    q = [a]

    while q:
        v = q.pop(0)
        print(v, end=' ')

        for i in range(len(graph[a])):
            if graph[v][i] == 1 and (i not in visited):
                # q에 추가하고 방문체크
                q.append(i)
                visited.append(i)


# stack을 이용한 재귀로 풀기
def dfs2(a):
    # 현재 노드 방문처리
    visited = [a]
    q = [a]

    while q:
        v = q.pop()
        print(v, end=' ')

        for i in range(len(graph[a])):
            if graph[v][i] == 1 and (i not in visited):
                # q에 추가하고 방문체크
                q.append(i)
                visited.append(i)


dfs2(V)
print()
bfs(V)
# print(visited)


# def dfs(a, visited):
#     # 현재 노드 방문처리
#     visited.append(a)
#     print(a, end=' ')
#
#     for i in range(len(graph[a])):
#         if graph[a][i] == 1 and (i not in visited):
#             dfs(i, visited)