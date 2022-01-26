def solution(absolutes, signs):
    ans = 0
    for i in range(len(signs)):
        ans = ans + absolutes[i] if signs[i] else ans - absolutes[i]
    return ans

##############
    # ans = 0
    #
    # for i in range(len(signs)):
    #     if signs[i]:  # true 면
    #         ans += absolutes[i]
    #     else:
    #         ans -= absolutes[i]
    #
    # return ans