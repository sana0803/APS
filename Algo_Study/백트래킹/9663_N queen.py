import sys
sys.stdin = open("input_9663.txt")

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를
# 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기

# def backtrack(v):
#     if promising(v):
#         if solution at v:
#             solution
#         else:
#             for i in v:
#                 backtrack(i)


def promising(n):
    # 이 위치가 유망한지 확인
    for i in range(n):  # idx = 행, board[i] = 열
        # (행끼리의 차(n-i) == 열끼리의 차의 절대값) = true면 대각선에 퀸 존재함
        if board[n] == board[i] or n - i == abs(board[n] - board[i]):
            return False    # 유망하지 않음
    return True


# 한줄씩 재귀하면서 backtrack 실행
def backtrack(m):   # m = 행번호
    global cnt

    if m == N:  # 마지막까지 탐색완료 == 각 행마다 퀸이 1개씩 배치됨
        cnt += 1

    else:
        # (m, i)에 퀸 놓기
        for i in range(N):  # i = 열번호 / 0부터 옮겨가면서 유망한곳 찾기
            board[m] = i    # board[0] = 0, 1, 2, 3....
            if promising(m):    # 행,열,대각선 체크 / true면 계속 진행
                backtrack(m + 1)    # 다음행으로 넘어가기
                

N = int(input())
# 퀸 위치 확인하기 위한 array
board = [0] * N     # ex: [1, 3, 2, 0] <- idx = 행, board[idx] = 열
cnt = 0
# print(board)

backtrack(0)
print(cnt)