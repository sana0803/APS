import sys
sys.stdin = open("input.txt")

# 배열의 크기 n, 숫자가 더해지는 횟수 m, 연속 가능한 수 k / 5 8 3
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print(arr)

max_num = arr[-1]
second_num = arr[-2]

cnt = 0
ans = 0
while cnt != m:
    for _ in range(k-1):
        ans += max_num
        cnt += 1

        if cnt == m:
            break
    if cnt == m:
        break
    ans += second_num
    cnt += 1

print(ans)
print(list(range(k)))