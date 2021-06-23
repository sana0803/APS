import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    num = list(map(int, input().split()))
    avg = sum(num) / len(num)

    print('#{}'.format(tc), end=' ')
    if avg < int(avg) + 0.5:
        print(int(avg))
    else:
        print(int(avg)+1)
