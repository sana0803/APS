import sys
sys.stdin = open("input_16987.txt")

N = int(input())    # 계란의 수
eggs = [list(map(int, input().split())) for _ in range(N)]   # 계란 내구도와 무게
# i+1번째 줄에는 왼쪽에서 i번째에 위치한 계란의 내구도 Si(1 ≤ Si ≤ 300)와
# 무게 Wi(1 ≤ Wi ≤ 300)가 한 칸의 빈칸을 사이에 두고 주어진다.
# 부딪히면 계란의 무게만큼 내구도 감소

# 7 5 -> 부딪힌 계란의 무게만큼 내구도 감소 => 7-4 = 3
# 3 4 -> 3-5 = -2 -> 0이하가 되면 깨짐
# 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨기
print(eggs)

visited = [0] * N
cnt = 0


def hit(start):
    global cnt

    # if
    for j in range(N):
        eggs[start][0] -= eggs[j][1]   # 내구도 깎기
        cnt += 1
        visited[j] = 1
        # hit()
        visited[j] = 0


for i in range(N):
    hit(i)