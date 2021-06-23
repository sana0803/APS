import sys
sys.stdin = open("input.txt", "r")

# for tc in range(1, int(input()) + 1):
#     a, b = map(int, input().split())
#     c = a // b
#     d = a % b
#     print('#{} {} {}'.format(tc, c, d))


############
for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print('#{}'.format(tc), *divmod(a, b))

