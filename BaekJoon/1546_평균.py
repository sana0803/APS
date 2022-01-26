import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

N = int(input())
score = list(map(int, input().split()))
M = max(score)

for i in range(len(score)):
    score[i] = (score[i] / M) * 100
sum_score = sum(score)
avg = sum_score / N
print(avg)