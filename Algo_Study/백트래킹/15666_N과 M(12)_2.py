import sys
sys.stdin = open("input_11663.txt")

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 오름차순 만들기
print(arr)
res = {}
ans = []


def make_num(idx):  # idx = 0
    global ans, res

    if 1 < idx <= M:
        if ans[idx-1] < ans[idx-2]:  # 앞숫자가 뒤 숫자보다 더 크면
            return

    # 종료조건
    if len(ans) == M:    # 수열 갯수 채웠으면
        print('갯수 채움', ans)
        if res.get(tuple(ans), 0) == 0:  # 같은 값이 없을때만 추가
            res[tuple(ans)] = 0
        # print('res', res)
        return res

    # 반복
    # num = -1
    for i in range(N):
        # if num != arr[i]:  # 중복 숫자인지 체크
        ans.append(arr[i])
        # num = arr[i]    # 중복 체크를 위해 갱신
        make_num(idx+1)
        ans.pop()


make_num(0)
# print(res.keys())
print(sorted(res.keys()))
print('res', res)
for j in sorted(res.keys()):
    print(*j)
