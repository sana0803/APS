import sys
sys.stdin = open("input_2615.txt")
# from pandas import DataFrame

# 19개의 가로세로줄
# 검은색 win 1, 흰색 win 2, 아직 승부x 0
# 이긴 돌 중 가장 왼쪽에 있는 바둑알의 r, c 좌표 구하기

board = [list(map(int, input().split())) for _ in range(19)]
# print(DataFrame(board))

# 위 > 아래, 왼 > 오 순서대로 보기때문에 모두 다 확인할 필요 없음
# 왼쪽 하단 검색하는거 추가하기
dr = [1, 1, 0, -1]    # 하(↓), 우하(⬊), 우(➞), 우상(⬈), 좌하
dc = [0, 1, 1, 1]

# 숫자별로 갯수를 세서 먼저 5가 되는 쪽을 승리로?
# 6개 이상 연속된 경우는 X
visited = [[0] * 19 for _ in range(19)]


def omok():
    for r in range(19):
        for c in range(19):
            # 바둑판 탐색하면서 1이나 2가 놓여있다면 4방 탐색
            if board[r][c] > 0:
                visited[r][c] = 1   # 방문체크
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    cnt = 1     # 연속된 바둑알 세기
                    # index 범위 안이고 방문 안했다면 + 같은 색이라면
                    while 0 <= nr < 19 and 0 <= nc < 19 and visited[nr][nc] == 0 and board[r][c] == board[nr][nc]:
                        cnt += 1    # 갯수세기
                        visited[nr][nc] = 1     # 방문체크
                        nr += dr[i]
                        nc += dc[i]

                        if cnt == 5:    # 5개가 됐을때
                            # 6개 이상인지
                            if 0 <= nr + dr[i] < 19 and 0 <= nc + dc[i] < 19 and board[nr][nc] == board[nr + dr[i]][nc + dc[i]]:
                                break
                            elif 0 <= r - dr[i] < 19 and 0 <= c - dc[i] < 19 and board[r][c] == board[r - dr[i]][c - dc[i]]:
                                break
                            return board[r][c], r+1, c+1

    return 0, -1, -1    # 승부 안 나면


win, x, y = omok()
if not win:  # 승부 안 남
    print(win)
else:
    print(win)
    print(x, y)

