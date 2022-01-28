import sys
sys.stdin = open("input.txt")

N = int(input())
num = list(int(input()) for _ in range(N))

num.sort()
for i in num:
    print(i)