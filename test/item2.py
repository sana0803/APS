import sys
sys.stdin = open("input_2.txt")
# 팰린드롬, 문자열 S가 주어졌을때 S의 부분문자열 중 가장 긴 팰린드롬 구하기
s = [input() for _ in range(4)]
print(s)
# 가능한 한 모든 문자열을 선택해서 팰린드롬인지 확인
# abcdcba

def solution(text):
    for i in range(len(text)):
        for j in range(i + 1):
            tmp = text[j:len(text) - i + j]
            if tmp == tmp[::-1]:    # 팰린드롬이면
                print(tmp)
                return tmp


for char in s:
    solution(char)