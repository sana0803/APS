# 최소비용으로 그 금액만큼의 동전 생산
# 이거 그리디인가?
# 생산할 금액 money, 6종류 동전의 생산단가를 나타내는 정수 배열 costs
# 차례대로 1 5 10 50 100 500원의 단가


def solution(money, costs):
    coins = [500, 100, 50, 10, 5, 1]
    costs = costs[::-1] # 거꾸로 돌려주기
    ans = 0

    for i in range(len(coins)):
        cnt = 0
        cnt += money // coins[i]    # 큰 순서대로 몇개가 필요한지 세기
        for j in range(len(costs)): # 다음 가격과 비교하기
            if i > j or i == j:
                continue
            while cnt > -1:
                # 최대 cnt * 생산비용보다 다음 생산비가 싸면
                if (costs[i] * cnt) > (costs[j] * (coins[i] // coins[j]) * cnt):
                    cnt -= 1
                else:
                    break

        money -= (coins[i] * cnt)   # 돈 빼서 없애기
        ans += (costs[i] * cnt)
        print(money, ans)
    return ans


solution(4578, [1, 4, 99, 35, 50, 1000])


