# def solution(s):
#     answer = ''
#     txt = s.split(' ')
#     for i in range(len(txt)):
#         for j in range(len(txt[i])):
#             if j % 2:  # 홀수 idx
#                 answer += txt[i][j].lower()
#             else:  # 짝수 idx
#                 answer += txt[i][j].upper()
#         answer += ' '
#     return answer[:-1]


####
def solution(s):
    s_list = list(s.title())
    tmp = -1
    for i in range(len(s_list)):
        if s_list[i].isupper():
            tmp = i
        elif not (i-tmp) % 2: # 짝수일때
            s_list[i] = s[i].upper()
    return ''.join(s_list)


print(solution('try hell world'))