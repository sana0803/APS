import sys
sys.stdin = open("input.txt")

# 괄호를 쳐서 식의 값을 최소로 만드는 프로그램
# 마이너스(-)를 만날때 가장 큰 수를 빼기

arr = input().split('-')
ans = 0

for i in arr[0].split('+'):
    print(i)
    ans += int(i)

for i in arr[1:]:
    print(i)
    for j in i.split('+'):
        ans -= int(j)

print(ans)