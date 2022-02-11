import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline  # pypy로 제출할때는 이렇게

t = int(input())

for _ in range(t):
    n = int(input())
    worker = [list(map(int, input().split())) for _ in range(n)]
    worker.sort()
    print(worker)

    min_rank = worker[0][1]
    cnt = 1
    for i in range(n):
        rank = worker[i][1]
        if rank < min_rank:
            min_rank = rank
            cnt += 1

    print(cnt)

