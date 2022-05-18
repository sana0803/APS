# import sys
# sys.stdin = open("input_10971.txt")
# 7명 난쟁이 키의 합이 100
ans = []
visited = [0] * 9

def solution(arr, idx):
    global ans
    if sum(ans) > 100 or idx > 8:
        return

    if len(ans) == 7 and sum(ans) == 100:
        print('13번 줄', ans)
        return ans

    for i in range(idx, len(arr)):
        if not visited[i]:
            visited[i] = 1
            ans.append(arr[i])
            print(idx, arr[i], ans)
            solution(arr, idx+1)
            visited[i] = 0
            ans.pop()
            print('21번', ans)

    return ans


solution([20, 7, 23, 19, 10, 15, 25, 8, 13], 0)
print('최종:', sum(ans))