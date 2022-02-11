import sys
sys.stdin = open("input.txt")

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
print(maze)
cnt = 0

for i in range(n):
    for j in range(m):
        here = maze[0][0]
        for k in range(4):  # 4방향 탐색
            cur_n = i + dr[k]
            cur_c = j + dc[k]
            if 0 <= cur_n < n and 0 <= cur_c < m:
                if maze[cur_n][cur_c] == 1:
                    cnt += 1
                elif maze[cur_n][cur_c] == 0:
                    break
            else:
                break

print(cnt)