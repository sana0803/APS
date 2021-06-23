import sys
sys.stdin = open("input.txt", "r")

N = input()
ans = 0
for i in N:
    ans += int(i)

print(ans)