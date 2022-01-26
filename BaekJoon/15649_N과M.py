# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# def solution(n, m):
#     for i in range(1, n+1):
#         print(i)
#         for j in range(m+1):
#             arr = [0] * m
#             # arr[i] = i
#             # print(j)
#             num = 0
#             if i == j:
#                 continue
#             else:
#                 arr.append(j)
#                 print(arr)
#
# print(solution(4, 2))

import sys
sys.stdin = open("input.txt")

# print(input().split())
n, m = list(map(int, input().split()))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        print('for문 돈다', i)
        if i not in s:
            print('s가 없다')
            s.append(i)
            print(s, i, '33번째줄')
            dfs()
            print('dfs 재귀')
            s.pop()
            print(s, i, 'pop했다')

dfs()