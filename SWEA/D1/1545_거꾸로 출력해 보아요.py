import sys
sys.stdin = open("input.txt", "r")

# N = int(input())
# ans = []
# for i in range(N + 1):
#     ans.append(N - i)
#
# print(*ans)

N = 8
ans = list(range(N+1))[::-1]

print(*ans)