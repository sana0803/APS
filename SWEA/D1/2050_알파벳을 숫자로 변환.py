import sys
sys.stdin = open("input.txt", "r")

text = input()
for i in range(len(text)):
    print(ord(text[i]) - 64, end=' ')

