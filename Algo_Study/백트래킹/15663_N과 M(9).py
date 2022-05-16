import sys
sys.stdin = open("input_11663.txt")

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 오름차순 만들기

print('첫 배열', arr)
# N개의 자연수 중에서 M개를 고른 수열
visited = [0] * N
res = []
ans = []


def make_num():  # idx = 0
    global ans, res

    # 종료조건
    if len(ans) == M:    # 수열 갯수 채웠으면
        print('갯수 채움', ans)
        print('현재 res', res)
        tmp = ' '.join(map(str, ans))   # ans arr 상태로하면 중복 검사가 안됨ㅠㅠ
        print('tmp', tmp)
        # print(*ans)
        # if ans not in res:
        #     print('ans가 res에 없다')
        #     res.append(ans[:])
        #     print('res', res)
        if tmp not in res:
            res.append(tmp)
            print('res', res)
        return res

    # 반복
    for i in range(N):  # [1 7 9 9]
        if not visited[i]:  # 방문하지 않았으면
            # print('여기 시작', i)
            visited[i] = 1
            ans.append(arr[i])
            print('ans', ans)
            # print('visited', visited)
            make_num()
            ans.pop()
            print('pop', ans)
            visited[i] = 0


make_num()

for j in res:
    print(j)






