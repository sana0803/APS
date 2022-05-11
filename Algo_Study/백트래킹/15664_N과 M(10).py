import sys
sys.stdin = open("input_11663.txt")

import sys
sys.stdin = open("input_11663.txt")

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 오름차순 만들기
# 수열 비내림차순
print('첫 배열', arr)
# N개의 자연수 중에서 M개를 고른 수열
visited = [0] * N
res = []
ans = []


def make_num(idx):  # idx = 0
    global ans, res
    print('지금 ans', idx, ans)

    # 가지치기
    if 1 < idx <= M:    # 현재 idx에서 이전 idx에 더 작은숫자가 있으면 pass
        if ans[idx-1] < ans[idx-2]:
            return

    # 종료조건
    if len(ans) == M:    # 수열 갯수 채웠으면
        # if ans[0] > ans[1]: # 조건에 맞지 않음(앞자리가 더 큼)
        #     return

        print('갯수 채움', ans)
        print('현재 res', res)
        tmp = ' '.join(map(str, ans))   # ans arr 상태로하면 중복 검사가 안됨ㅠㅠ
        print('tmp', tmp)
        # print(*ans)
        if tmp not in res:
            res.append(tmp)
            print('res', res)
        return res

    # 반복
    for i in range(N):
        if not visited[i]:  # 방문하지 않았으면
            # print('여기 시작', i)
            visited[i] = 1
            ans.append(arr[i])
            # print('ans', ans)
            # print('visited', visited)
            make_num(idx + 1)
            ans.pop()
            print('pop', ans)
            visited[i] = 0


make_num(0)

for j in res:
    print(j)






