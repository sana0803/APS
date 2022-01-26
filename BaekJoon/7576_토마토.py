import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# arr = [[0 for _ in range(M)] for _ in range(N)]

# 익은 토마토 1, 익지않은 토마토 0, 빈칸 -1
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, -1, 1] # 상하좌우
dc = [-1, 1, 0, 0]

print(DataFrame(box))

def bfs():
    for i in range(4):
        dr = cur_r

