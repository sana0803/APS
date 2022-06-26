import sys
sys.stdin = open("input_14888.txt")

n = int(input())    #  N(2 ≤ N ≤ 11)
numbers = list(map(int, input().split()))
# 연산자 리스트
operator = list(map(int, input().split()))
visited = [-1] * 12  # N의 갯수가 최대 11개라서 그대로 연산자 집어넣기
max_num, min_num = -100000000, 1000000000
ans = numbers[0]
print(numbers, operator)


def calc(cnt):
    global ans, max_num, min_num

    # 종료조건
    if cnt == (n - 1):    # 숫자를 다 돌았을때
        for j in range(n - 1):
            if visited[j] == 0:     # 더하기
                ans += numbers[j+1]
            elif visited[j] == 1:   # 빼기
                ans -= numbers[j+1]
            elif visited[j] == 2:   # 곱하기
                ans *= numbers[j+1]
            elif visited[j] == 3:   # 나누기
                ans = int(ans / numbers[j+1])
        min_num = min(ans, min_num)
        max_num = max(ans, max_num)
        return

    # 반복
    for i in range(4):
        if operator[i] > 0:  # 연산자가 있다면
            operator[i] -= 1  # 계산 횟수 빼기
            visited[cnt] = i  # 몇번째 연산자인지 집어넣기
            print(visited)
            calc(cnt+1)
            operator[i] += 1  # 되돌리기


calc(0)
print(max_num)
print(min_num)