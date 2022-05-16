import sys
sys.stdin = open("input_11663.txt")

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 오름차순 만들기

print(arr)
visited = [0] * N
res = []
ans = []


def make_num():  # idx = 0
    global ans, res

    # 종료조건
    if len(ans) == M:    # 수열 갯수 채웠으면
        # print('갯수 채움', ans)
        tmp = ' '.join(map(str, ans))   # ans arr 상태로하면 중복 검사가 안됨ㅠㅠ
        print('tmp', tmp)
        res.append(tmp)
        print('res', res)
        return res

    # 반복
    num = -1
    for i in range(N):  # [1 1 2 2]
        if num != arr[i]:  # 중복 숫자인지 체크
            print('여기 시작', i)
            ans.append(arr[i])
            num = arr[i]    # 중복 체크를 위해 갱신
            print('ans', ans)
            make_num()
            ans.pop()


make_num()

for j in res:
    print(j)
