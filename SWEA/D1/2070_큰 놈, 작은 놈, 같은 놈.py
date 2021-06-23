import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    a, b = (map(int, input().split()))

    print('#{}'.format(tc), end=' ')
    if a > b:
        print('>')

    elif a == b:
        print('=')

    else:
        print('<')