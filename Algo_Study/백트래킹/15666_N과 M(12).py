import sys
sys.stdin = open("input_11663.txt")

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 오름차순 만들기

# print(arr)
visited = [0] * N
res = []
ans = []


def make_num(idx):  # idx = 0
    global ans, res

    if 1 < idx <= M:
        if ans[idx-1] < ans[idx-2]:
            return

    # 종료조건
    if len(ans) == M:    # 수열 갯수 채웠으면
        # print('갯수 채움', ans)
        tmp = ' '.join(map(str, ans))
        res.append(tmp)
        # print('res', res)
        return res

    # 반복
    num = -1
    for i in range(N):
        if num != arr[i]:  # 중복 숫자인지 체크
            ans.append(arr[i])
            num = arr[i]    # 중복 체크를 위해 갱신
            make_num(idx+1)
            ans.pop()


make_num(0)

for j in res:
    print(j)
