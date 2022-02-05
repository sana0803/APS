import sys
sys.stdin = open("input.txt")

# 제일 왼쪽 -> 오른쪽 최소 비용 계산
# 17점 : 1원
# 41점 : 2 ≤ N ≤ 1,000, 제일 왼쪽 도시 -> 제일 오른쪽 도시
# 거리 최대 10,000, 리터 당 가격은 최대 10,000
# 42점 : 아무 제약 x

n = int(input()) # 도시의 개수
dist = list(map(int, input().split()))  # 도시 연결하는 길이
cost = list(map(int, input().split()))  # 주유소 리터당 가격
ans = 0
# print(dist, cost)

min_cost = cost[0]
for i in range(n - 1):
    if min_cost > cost[i]:
        min_cost = cost[i] # 최소 가격 갱신
    ans += min_cost * dist[i]

print(ans)