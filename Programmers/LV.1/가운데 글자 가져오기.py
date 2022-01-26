def solution(s):
    mid = len(s) // 2

    #     if len(s) % 2:
    #         return s[mid]

    #     else:
    #         return  s[mid - 1] + s[mid]

    return s[mid] if len(s) % 2 else s[mid - 1] + s[mid]