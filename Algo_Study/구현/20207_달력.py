import sys
sys.stdin = open("input_20207.txt")

# 연속된 두 일자에 각각 일정이 1개 이상 있다면 일정이 연속되었다고 표현
# 연속된 모든 일정은 하나의 직사각형에 포함
# 연속된 일정을 모두 감싸는 작은 직사각형의 크기만큼 코팅지 자름

# n = 일정 개수 / s = 시작날짜 / e = 종료날짜

n = int(input())
calender = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        calender[i] += 1   # 일정 표시하기

# print(calender)
width = 0
height = 0
ans = 0

for i in range(1, 366):
    if calender[i] == 1:
        width += 1

print(width)

