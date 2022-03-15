# https://www.acmicpc.net/problem/14888
import sys
sys.stdin = open("input3.txt")

N = int(input())
nums = list(map(int, input().split()))

# 각각의 연산자 갯수를 저장
add, sub, mul, div = map(int, input().split())  # +, -, *, //

max_num = 999999999
min_num = -99999999


def dfs(i, res, add, sub, mul, div):
    # 3 6 0 1 1 1
    global max_num, min_num
    
    # 종료조건
    if i == N:
        if res > max_num:
            max_num = res
        if res < min_num:
            min_num = res
        return

    # 재귀
    # 각 연산자 별로 돌릴때마다 -1 해서 줄임
    # 다음 인덱스 값인 i+1를 넘겨준다
    else:
        if add:
            dfs(i + 1, res + nums[i], add - 1, sub, mul, div)
        if sub:
        # 2 1 1 1
            dfs(i + 1, res - nums[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, res * nums[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(res / nums[i]), add, sub, mul, div - 1)


dfs(1, nums[0], add, sub, mul, div)
print(max_num)
print(min_num)