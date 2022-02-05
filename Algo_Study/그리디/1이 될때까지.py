import sys
sys.stdin = open("input.txt")

# n이 1이 될때까지 다음 둘 중 하나만 반복적으로 선택해 수행
# n에서 1을 뺀다 / n을 k로 나눈다. (n이 k로 나누어떨어질 때만)

n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)