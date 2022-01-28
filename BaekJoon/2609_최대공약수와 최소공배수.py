import sys

sys.stdin = open("input.txt")
# from pandas import DataFrame

N, M = map(int, input().split())

GCD = []  # 최대공약수
ans = []

gcd_num = 1
for _ in range(N):
    if N % gcd_num == 0:
        GCD.append(gcd_num)

    gcd_num += 1

for i in GCD[::-1]:  # 최대공약수 찾기
    if M % i == 0:
        ans.append(i)
        ans.append(int(N * M / i))  # 최소공배수
        break

for j in ans:
    print(j)


# 유클리드 호제법으로 최대 공약수 찾기
# 참고 https://goplanit.site/22.%20Algorithm(2609_py)/

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        # print(a, b)
    return a  # 최대 공약수

gcd(N, M)
