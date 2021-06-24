# 리스트 컴프리헨션
# [ㅁㅁㅁ for ㅁ in ㅁㅁㅁ]

def solution(n):
    return [int(i) for i in str(n)[::-1]]

    ######
    # answer = []
    # for i in str(n)[::-1]:
    #     answer.append(int(i))
    # return answer