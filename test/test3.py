# 맨하탄 거리(수평거리+수직거리)가 다를경우 더 가까운쪽의 손가락으로 키 누르기
# 왼손은 0, 오른손은 1
# 처음 위치 왼손 'Q', 오른손 'Y'
# 맨하탄거리가 같을 경우 수평거리가 더 가까운쪽 손가락 이용
# 수평거리도 동일하면 키보드 왼쪽 (idx 0~4)는 왼손, 오른쪽 (idx 5~9)는 오른손

def solution(line):
    answer = []
    qwerty = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
              ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
    hands = ['Q', 'P']   # 왼손 오른손 위치
    manhattan = 0   # 맨하탄, 수평거리
    horizon_dist = 0

    print(qwerty)
    for i in range(len(line)):
        print('인풋', line[i])
        for j in range(2):
            if line[i] in qwerty[j]:    # 여기에 있으면 여기서 찾기
                print(qwerty[j].index(line[i]))
                horizon_dist = qwerty[j].index(hands[0])
                print(horizon_dist)
                # for k in range(10):
            else:
                continue
    return answer

solution("Q4OYPI")
# [0,0,1,0,1,1]
# "RYI76"	[0,0,1,1,0]
# "64E2"	[1,1,1,0]