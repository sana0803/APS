import sys
sys.stdin = open("input_14712.txt")
from pandas import DataFrame

# 격자 행의 개수 n, 열의 개수 m
N, M = map(int, input().split())
# 없앨수 있는 넴모가 없을때 넴모 배치의 가짓수 구하기
# dr = [0, 0, -1, 1]
# dc = [1, -1, 0, 0]
# 넴모를 놓았을때 2x2가 되면 안됨
box = [[0] * (M+1) for _ in range(N+1)]
print(box)
ans = 0


def nemo(i, j): # (행, 열)
    global ans

    if j > M:   # 열이 M보다 커지면 다음 행 넘어가기, j 리셋
        i, j = i+1, 1

    # 종료조건 : 행이 N보다 커지면
    if i > N:
        ans += 1
        print('2. 종료상태' + '\n', DataFrame(box))
        print('25번 줄 ans', ans)
        return ans

    # 반복
    # 주변에 놓을수 있는지 확인 (왼, 위, 좌상)
    # box[i][j]가 0일때 / 1일때 둘다 재귀 들어가야해서 2번 nemo 호출해야함
    nemo(i, j+1)    # box[i][j] = 0 인 상태 재귀
    if box[i-1][j] == 0 or box[i][j-1] == 0 or box[i-1][j-1] == 0:
        box[i][j] = 1
        # ans += 1   # ???
        # print('1. 현재상태' + '\n', DataFrame(box))
        # print('ans 값:', ans)
        nemo(i, j+1)    # box[i][j] = 1 인 상태 재귀
        box[i][j] = 0   # 리셋해주기
    # print('ans 값2:', ans)


nemo(1, 1)
print('최종 ans :', ans)