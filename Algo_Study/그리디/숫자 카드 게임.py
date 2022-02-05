import sys
sys.stdin = open("input.txt")

# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장 뽑기
# n = 행 / m = 열

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(arr)
num = 0
for i in arr:
    if num <= min(i):
        num = min(i)
    else:
        continue

print(num)