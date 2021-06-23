import sys
sys.stdin = open("input.txt", "r")

# for tc in range(1, int(input()) + 1):
N = int(input())
ans = []
for i in range(N + 1):
    ans.append(2 ** i)
print(*ans)
