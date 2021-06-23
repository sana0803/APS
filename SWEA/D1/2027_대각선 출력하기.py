# import sys
# sys.stdin = open("input.txt", "r")

for i in range(5):
    text = ['+'] * 5
    text[i] =  '#'
    print(''.join(text))

for n in range(5):
    txt = '+'*n + '#' + '+'*(4-n)
    print(txt)