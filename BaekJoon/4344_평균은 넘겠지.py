import sys
sys.stdin = open("input.txt")

C = int(input())
for i in range(C):
    arr = list(map(int, input().split()))
    N = arr[0]

    del arr[0] # N을 뺀 나머지 평균 구하기
    avg = sum(arr) / N
    cnt = 0

    for j in arr:
        if j > avg:
            cnt += 1

    ans = cnt / N * 100

    # print(str(round(ans, 3)) + '%') 이렇게 하면 40.0% 때문에 틀림
    print('{:.3f}%'.format(ans))