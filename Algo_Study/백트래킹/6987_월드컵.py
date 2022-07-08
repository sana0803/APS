import sys
sys.stdin = open("input_6987.txt")

# 월드컵 조별 최종 예선에서 6개국이 각 조별로
# 동일한 조에 소속된 국가들과 한번씩 총 5번 경기를 치른다
# 각 나라의 승, 무승부, 패의 수
# 결과가 가능하면 1, 불가능하면 0

# 승 / 패
# 무승부 / 무승부
# 패 / 승
arr = [list(map(int, input().split())) for _ in range(4)]
print(arr)

# def back():
    # ??


