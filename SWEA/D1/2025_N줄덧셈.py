import sys
sys.stdin = open("input.txt", "r")

N = int(input())
print(sum(range(N+1)))

####################
# N = list(range(1, int(input()) + 1))
# print(sum(N))

####################
# ans = 0
# for i in range(1, N+1):
#     ans += i
# print(ans)
