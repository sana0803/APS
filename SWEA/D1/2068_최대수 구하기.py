import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    num = list(map(int, input().split()))

    print('#{}'.format(tc), max(num))