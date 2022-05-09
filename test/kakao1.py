import sys
sys.stdin = open("input_1.txt")
# RT/CF/JM/AN
# 선택지 7개 / 점수 많은거로 성격유형 판단 / 점수가 같으면 사전순으로 빠른 성격 유형 출력
# survey = 1차원 문자배열 / choice = 선택지 1차원 정수배열
# RT <- idx: 0은 비동의 / 1이 동의
# CHOICE = 1 매우 비동의 ~ 7 매우 동의
# 1 = survey[i][0] 3점, 2 = 2점, 3 = 1점, 4 = 0점
# 5 = survey[i][1] 1점, 6 = 2점, 7 = 3점

def solution(survey, choices):
    answer = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    types = ['RT', 'CF', 'JM', 'AN']
    res = ''

    for i in range(len(survey)):
        if choices[i] < 4:  # 비동의일 경우
            if choices[i] == 1:
                answer[survey[i][0]] = answer[survey[i][0]] + 3
            elif choices[i] == 2:
                answer[survey[i][0]] = answer[survey[i][0]] + 2
            else:
                answer[survey[i][0]] = answer[survey[i][0]] + 1

        elif choices[i] == 4:   # 중간
            continue

        elif choices[i] > 4:    # 동의
            answer[survey[i][1]] = answer[survey[i][1]] + (choices[i]-4)

    for j in range(len(types)):
        if answer[types[j][0]] > answer[types[j][1]]:
            res += types[j][0]
        elif answer[types[j][0]] < answer[types[j][1]]:
            res += types[j][1]
        else:   # 값이 같으면
            res += types[j][0]

    return res


solution(["TR", "RT", "TR"], [7, 1, 3])