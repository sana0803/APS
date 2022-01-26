# def solution(s, n):
#     ans = ''
#
#     # s 바꿀 문장
#     # n만큼 옆으로 밀기
#     # 소문자는 97부터
#     # 대문자는 65부터
#     for i in s:
#         if i.isupper():
#             num = ord(i)
#             ans += chr((num - 65) % 26 + n)
#
#         elif i.islower():
#             num = ord(i)
#             ans += chr((num - 97) % 26 + n)
#
#         else:
#             ans += i
#
#     return ans

s = 'a B z'
n = 4
ans = ''
for i in s:
    if i.isupper():
        num = ord(i) - 65
        ans += chr((num % 66) + n)

    elif i.islower():
        num = ord(i) - 97
        ans += chr((num % 98) + n)

    else:
        ans += i
print(ans)


# print(solution('a B z', 1))