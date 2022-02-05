import sys
sys.stdin = open("input.txt")

# 공포도 측정

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr)

