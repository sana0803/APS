import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    date = input()
    y = date[0:4]
    m = date[4:6]
    d = date[6:8]

    ans = y + '/' + m + '/' + d
    print('#{}'.format(tc), end=' ')
    if m == '02' :
        if int(d) < 29:
            print(ans)
        else:
            print(-1)

    elif m in ['04', '06', '09', '11']:
        if int(d) < 31:
            print(ans)
        else:
            print(-1)

    elif m in ['01', '03', '05', '07', '08', '10', '12']:
        if int(d) < 32:
            print(ans)
        else:
            print(-1)

    else:
        print(-1)
