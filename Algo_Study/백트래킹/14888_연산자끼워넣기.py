import sys
sys.stdin = open("input3.txt")

n = int(input())
numbers = list(map(int, input().split()))
# 각각의 갯수를 저장
add, sub, mul, div = map(int, input().split())
max_num, min_num = -100000000, 1000000000
