import sys
sys.stdin = open("input.txt", "r")

# A, B = map(int, input().split())
#
# if A > B:
#     print('A')
# elif B > A:
#     print('B')
# elif A == 3 and B == 1:
#     print('B')
# elif B == 3 and A == 1:
#     print('A')

##########
a, b = map(int, input().split())

result = { 1 : 'A', -1 : 'B', 2 : 'B' , -2 : 'A' }
print(result[a - b])


# 메모리: 52,932kb 실행시간: 132ms
print('AB'[input() in ['1 2','2 3','3 1']])

# 메모리: 48,048 kb 실행시간: 115 ms
print(input() in ['2 1','1 3','3 2'] and 'A' or 'B')