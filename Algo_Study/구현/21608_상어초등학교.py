import sys
sys.stdin = open("input_21608.txt")
# from pandas import DataFrame

# N = 교실 크기, N*N / 학생 수 N**2
# 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함.
# 2. 1을 만족하는 칸이 여러 개면, 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 자리를 정함.
# 3. 2를 만족하는 칸도 여러 개라면 행 번호가 가장 작은 칸,
# 그러한 칸도 여러 개면 열 번호가 가장 작은 칸으로 자리 정함.
# 조건에 맞춰 학생 앉힌 후 학생의 만족도 구하기 = 인접하게 앉은 좋아하는 학생수 구하기
# 0 = 0 / 1 = 1 / 2 = 10 / 3 = 100 / 4 = 1000
# 학생 만족도의 총합 구하기

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

N = int(input())
classroom = [[0] * N for _ in range(N)]
student = N ** 2
like_student = [[] for _ in range(student+1)]

# 좋아하는 학생 번호별로 list에 넣어주기
for _ in range(student):
    arr = list(map(int, input().split()))
    like_num = arr[1:]  # 좋아하는 학생번호
    like_student[arr[0]] = like_num    # 각자 번호에 선호 학생 넣어주기
    # print(like_student)

    max_friend = -1
    max_empty = -1
    min_r = -1
    min_c = -1
    for r in range(N):
        for c in range(N):
            if classroom[r][c] == 0:    # 비어있으면 4방 체크
                friend_cnt = 0    # 좋아하는 학생수 세기
                empty_cnt = 0   # 빈자리 세기
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 범위 넘어가는지 확인
                    if 0 <= nr < N and 0 <= nc < N:
                        # 좋아하는 학생 번호가 자리에 있는지 확인
                        if classroom[nr][nc] in like_num:   # 친구 +1
                            friend_cnt += 1
                        elif classroom[nr][nc] == 0:    # 빈 자리면 빈자리 +1
                            empty_cnt += 1

                # friend_cnt, empty_cnt 는 크고 r, c는 작은 곳일수록 정답
                # for문이 차례대로 돌기때문에 r, c는 어차피 작은숫자부터 시작함
                if max_friend < friend_cnt or (max_friend == friend_cnt and max_empty < empty_cnt):
                    # 갱신하기
                    max_friend = friend_cnt
                    max_empty = empty_cnt
                    min_r = r
                    min_c = c
    classroom[min_r][min_c] = arr[0]    # 현재 학생 자리 배치하기

print(classroom)

# 만족도 조사
point = 0
for r in range(N):
    for c in range(N):
        ans = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 넘어가는지 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 근처에 좋아하는 친구가 있는지?
                if classroom[nr][nc] in like_student[classroom[r][c]]:
                    ans += 1
                # print(ans)
        if ans != 0:    # 친구가 있으면
            # 0 = 0 / 1 = 1 / 2 = 10 / 3 = 100 / 4 = 1000
            point += 10 ** (ans - 1)
print(point)
