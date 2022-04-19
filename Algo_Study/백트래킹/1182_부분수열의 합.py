import sys
sys.stdin = open("input_1182.txt")

# N개의 정수로 이루어진 수열이 있을 때,
# 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이
# S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

N, S = map(int, input().split())    # 5, 0
arr = list(map(int, input().split()))   # -7 -3 -2 5 8
result = 0


def backtrack(i, graph, total):     # 0, arr, -7
    global result, S, N
    if total == S:  # 더한 값이 S이면 res +1
        result += 1

    # graph(부분수열) 만들기
    for j in range(i+1, N): # idx를 하나씩 올려가며 계속 반복
        backtrack(j, graph, total + graph[j])   # 1, arr, -7+(-3)


for i in range(N):
    backtrack(i, arr, arr[i])

print(result)








# def backtrack(num, total):
#     global cnt
#     if num == N:
#         if total == S:  # 더한 값이 S이면 cnt +1
#             cnt += 1
#         return
#
#     backtrack(num+1, total)     # 해당 숫자를 더하지 않을 경우
#     backtrack(num+1, total+arr[num])    # 더할 경우
#
#
# backtrack(0, 0) # 모든 원소를 선택하지 않았을 때는 제외하기
#
# if S == 0:
#     print(cnt - 1)
# else:
#     print(cnt)