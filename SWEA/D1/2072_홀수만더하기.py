import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    S = list(map(int, input().split()))
    ans = 0
    for i in S:
        if i % 2:
            ans += i

    print('#{} {}'.format(tc, ans))