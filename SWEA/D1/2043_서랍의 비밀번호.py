import sys
sys.stdin = open("input.txt", "r")

# for tc in range(1, int(input()) + 1):
P, K = map(int, input().split())

print((P+1) - K)