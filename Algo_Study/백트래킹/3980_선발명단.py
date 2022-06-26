import sys
sys.stdin = open("input_3980.txt")
# 포지션 수는 최대 5개

def back(player, score):
    global max_score

    # 종료
    if player == 11:
        max_score = max(max_score, score)   # 점수 갱신
        return

    # 반복
    for i in range(11):
        if visited[i] or arr[player][i] == 0:    # 방문했거나 능력이 없음
            continue
        visited[i] = 1  # 방문체크
        position[player] = i    # 포지션 배치
        back(player+1, score+arr[player][i])
        visited[i] = 0
        position[player] = -1


N = int(input())    # 테케
for _ in range(N):
    arr = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    visited = [0] * 11  # 방문체크
    position = [-1] * 11  # 포지션
    print(arr)
    back(0, 0) # player 숫자
    print(max_score)