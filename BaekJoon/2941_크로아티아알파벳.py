import sys
sys.stdin = open("input.txt")

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
txt = input()

for i in croatia:
    txt = txt.replace(i, '*') # replace로 해당단어 전체 바꿔주기

print(len(txt))



