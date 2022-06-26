import sys
sys.stdin = open("input_16987.txt")

# 왼쪽에서부터 자리수가 감소하면 줄어드는 수
# n번째로 작은 줄어드는 수 구하기 / 없으면 -1
# n = int(input())
n = 19
number = []
ans = 0
res = []
# 앞자릿 수가 무조건 1부터 시작, 1~9 다 돈다음에 다음 자리에서 다시 0~9 도는식
# number[0] 은 0이 올수 없음


def calc(cnt):
    global ans, res
    # print('카운트', cnt)
    # 정답 저장
    if len(number) > 0:
        tmp = int(''.join(map(str, number)))
        res.append(tmp)
        # print('res', res)

    # 종료조건
    if len(res) == n:
        print('끝')
        return res

    # 반복
    for i in range(0, 10):
        if len(number) == 0 or number[-1] > i:    # 더 큰숫자면 패스하게 만듦
            number.append(i)
            print(number)
            calc(cnt+1)
            number.pop()


calc(0)
res = list(res)
res.sort()
if n > 1023:    # 전체 경우의 수가 1023 (2의 10승 -1)
    print(-1)

else:
    print(res[n - 1])