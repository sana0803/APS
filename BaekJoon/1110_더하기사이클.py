import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# input이 0보다 작으면 0+숫자
num = input()

if len(num) == 1:
    num = '0' + num

cnt = 1
ans = int(num[0]) + int(num[1])
str_ans = str(ans)
new_num = num[1] + str_ans[-1]

while new_num != num:
    ans = int(new_num[0]) + int(new_num[1])
    str_ans = str(ans)
    new_num = new_num[1] + str_ans[-1]

    cnt += 1

print(cnt)
