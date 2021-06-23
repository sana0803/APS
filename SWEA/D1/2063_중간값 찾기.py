import sys
sys.stdin = open("input.txt", "r")

# for tc in range(1, int(input()) + 1):
N = int(input())
score = list(map(int, input().split()))
score.sort()

mid = (N // 2)
print(score[mid])