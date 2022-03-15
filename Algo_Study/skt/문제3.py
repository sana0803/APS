# 최단거리 경로라고 하는걸 보니 BFS다 / 다익스트라
# 왼쪽 위, 오른쪽 아래를 잇는 대각선이므로
from pandas import DataFrame

dr = [-1, 1, 0, 0, -1]  # 상하좌우 / 왼쪽 대각선
dc = [0, 0, -1, 1, -1]

def solution(width, height, diagonals):
    maze = [[0] * (width+1) for _ in range(height+1)]
    # visited = [[0] * (width+1) for _ in range(height+1)]
    # print(visited)
    for line in diagonals:  # 대각선 위치 찾기
        maze[line[0]][(height+1)-line[1]] = maze[line[0]-1][(height)-line[1]] = 1

    # print(DataFrame(maze))
    q = [(0, height)]    # 시작위치
    maze[0][height] = -1  # 방문체크

    while q:
        r, c = q.pop(0)

        if maze[r][c] = 1:
            for i in range(5):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < height and 0 <= nc < width and not maze[nr][nc]:
                    q.append((nr, nc))
                    maze[nr][nc] = -1   # 방문체크

        else:

    return


# for r in range(height):
#     for c in range(width):
#         if visited[r][c] == 1:
#             bfs(r, c)
#             visited[r][c] = 0
#             cnt += 1
# (a+b)!/(a!b!) 경로수 공식
# 대각 19×17에 있을때
# 16×19 경우수 * 2
# (= 17×18 경우수)
# * 34×18 경우수
print(cnt)
# 최종 답에서 % 1000019
solution(2, 2, [[1,1],[2,2]]) # 답 12
