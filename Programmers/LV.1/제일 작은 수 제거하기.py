def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

    #######
    #min_num = min(arr)
    # for i in arr:
    #     if i == min_num:
    #         arr.remove(i)
    #
    # if arr: # arr이 비어있지 않을때
    #     return arr
    #
    # else:
    #     return [-1]

