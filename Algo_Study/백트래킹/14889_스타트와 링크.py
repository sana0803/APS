import sys
sys.stdin = open("input_14889.txt")
# i번, j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치 = Sij
# 팀의 능력치는 그 값을 모두 더한것
# 팀의 능력치 차이를 최소화하기


def score_diff(team_1, team_2):  # 팀 점수 차이 구하기
    team1_score = 0
    team2_score = 0

    for i in range(len(team_1)):
        for j in range(len(team_1)):
            team1_score += arr[team_1[i]][team_1[j]]
            team2_score += arr[team_2[i]][team_2[j]]

    return abs(team1_score - team2_score)


def backtrack(team_1, score, idx):    # idx 번 사람이 팀 짰을 경우
    global ans

    # 팀1에서 팀 구성이 완료됐으면 중지하고 팀2 만들기
    if len(team_1) == N // 2:
        team_2 = []
        for i in range(N):
            if i not in team_1:  # 팀1에 없으면 team2 인원에 넣기
                team_2.append(i)
                print('팀2', team_2)

        min_score = score_diff(team_1, team_2)
        ans = min(ans, min_score)   # 최소 비교해서 답 리턴
        return

    for i in range(idx, N):
        if i not in team_1:     # 아직 없는 팀원이면
            team_1.append(i)    # 팀원에 넣기
            print('팀1', team_1)
            backtrack(team_1, score, i+1)   # 다시 팀구성
            team_1.remove(i)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 999
print(arr)

backtrack([], 0, 0)

print(ans)