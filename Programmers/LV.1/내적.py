# 내적 : 각 요소들을 순서대로 곱한 다음 더한 값

def solution(a, b):
    ans = 0

    for i in range(len(a)):
        ans += a[i] * b[i]

    return ans