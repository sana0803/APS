import sys
sys.stdin = open("input_14467.txt")

# 관찰 횟수 N / 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져있음
# 소는 1~10 / 소의 위치는 왼쪽 0 오른쪽 1 둘중 하나
# 소가 최소 몇 번 길을 건넜는지?
# 같은 번호의 소가 위치를 몇번 바꿨는지 세기

N = int(input())
observe = [list(map(int, input().split())) for _ in range(N)]
# print(observe)

# 처음 소 위치
cows_position = [-1] * 11
cnt = 0

for i in range(N):
    cow, position = observe[i][0], observe[i][1]

    if cows_position[cow] == -1:
        cows_position[cow] = position    # 소 현재위치 저장

    elif cows_position[cow] != position:    # 위치 옮겼다면
        cnt += 1
        cows_position[cow] = position   # 위치 옮겼으니 위치 갱신

print(cnt)