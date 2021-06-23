import sys
sys.stdin = open("input.txt", "r")

# for tc in range(1, int(input()) + 1):
N = int(input())
ans = set()
for num in range(1, int(N/2)):
    if N % num == 0:
        ans.add(num)
        ans.add(N // num)

print(*sorted(list(ans)))

# N = int(input())
# ans = []
# for num in range(1, N+1):
#     if N % num == 0:
#         ans.append(num)
# print(*ans)

# n=int(input())
# [print(i,end=' ') for i in range(1,n+1) if n%i==0]