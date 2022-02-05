import sys

sys.stdin = open("input.txt")

# t = 3개 합이 t 이하
# d = 배열

# d = [1, 4, 2, 6, 3] / t = 8

def triplets(t, d):
    d = sorted(d)   # [1, 2, 3, 4, 6]
    cnt = 0

    for i in range(len(d)-1):
        tmp = [0, 0, 0]
        tmp[0] = d[i]

        for j in range(i+1, len(d)):
            tmp[1] = d[j]
            left = 0
            right = len(d) - 1
            print(tmp, '21라인', cnt, left, right)

            while left <= right:
                mid = (left + right) // 2
                if tmp[0]+tmp[1] < t and d[mid] not in tmp:
                    tmp[2] = d[mid]

                    if tmp[0]+tmp[1]+tmp[2] > t:
                        right = mid-1
                        print(tmp, '30라인', cnt, left, right)

                    elif tmp[0]+tmp[1]+tmp[2] <= t:
                        cnt += 1
                        left = d[j+1]
                        print(tmp, '35라인', cnt, left, right)

                elif d[mid] in tmp:
                    left = mid+1

        if tmp[0] + tmp[1] >= t:
            break

    print(cnt)

triplets(8, [1, 4, 2, 6, 3])

