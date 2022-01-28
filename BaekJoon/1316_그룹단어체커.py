import sys
sys.stdin = open("input.txt")
# from pandas import DataFrame

N = int(input())
cnt = N
for _ in range(N):
    txt = input()
    for i in range(len(txt) - 1):
        print(txt.find(txt[i]), txt.find(txt[i + 1]))
        if txt.find(txt[i]) > txt.find(txt[i + 1]): # txt[i+1]이 이전에 나왔는지 확인
            # find()는 무조건 처음 나온 위치 반환
            cnt -= 1
            break

print(cnt)





        # if txt[j] != txt[j + 1]: # 뒤에 다른 문자가 오면 리스트에 넣기
        #     if txt[j] in letters: # list에 문자가 있다면 break
        #         break
        #
        #     else:
        #         letters.append(txt[j])
        #         print(letters)
        #
        # else:
        #     continue



