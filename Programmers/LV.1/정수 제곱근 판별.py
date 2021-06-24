def solution(n):
    ans = n ** (1 / 2)
    print(ans)
    if ans == int(ans):
        return (ans + 1) ** 2

    else:
        return -1   