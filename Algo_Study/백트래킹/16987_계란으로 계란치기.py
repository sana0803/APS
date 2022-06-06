import sys
sys.stdin = open("input_16987.txt")

N = int(input())    # 계란의 수
eggs = [list(map(int, input().split())) for _ in range(N)]   # [내구도, 무게]
# 부딪히면 계란의 무게만큼 내구도 감소
# 7 5 -> 부딪힌 계란의 무게만큼 내구도 감소 => 7-4 = 3
# 3 4 -> 3-5 = -2 -> 0이하가 되면 깨짐
# 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨기
print(eggs)
cnt = 0


def hit(start):
    global cnt
    print('깨진 계란:', cnt, '/', start)

    # 종료조건 (마지막 계란까지 살피면 종료)
    if start == N:
        res = 0
        for k in range(N):
            if eggs[k][0] <= 0:  # 깨진계란 세어보기
                res += 1
        print('24번째줄 cnt:', res)
        cnt = max(res, cnt)
        return cnt

    # 가지치기 (깨진 계란 패스), 다음 계란
    if eggs[start][0] <= 0:
        return hit(start+1)

    # 가지치기 (모든 계란이 깨져있으면 넘어감)
    tmp = True  # 계란이 깨져있는지 체크
    for j in range(N):
        # 자기번호는 넘어감 + 안 깨진게 1개라도 있다면
        if j == start:
            continue
        if eggs[j][0] > 0:
            tmp = False
            break
    if tmp:  # 모두 깨져있으면
        print('43번째 줄 cnt:', cnt)
        cnt = max(cnt, N-1)  # 자기빼고 다 깨져있으므로 n-1
        return

    for i in range(N):
        if eggs[start][0] <= 0 or eggs[i][0] <= 0:  # 계란이 깨졌다면
            continue
        if start != i:  # 자기 스스로는 칠수 없으므로 건너뛰기
            # 각각 때려서 내구도 깎기
            eggs[start][0] -= eggs[i][1]
            eggs[i][0] -= eggs[start][1]
            hit(start+1)
            # 되돌아 나와서 복구
            eggs[start][0] += eggs[i][1]
            eggs[i][0] += eggs[start][1]


hit(0)
print(cnt)