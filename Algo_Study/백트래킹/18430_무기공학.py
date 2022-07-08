import sys
sys.stdin = open("input_18430.txt")
# 길동이가 만들 수 있는 부메랑의 강도 합의 최댓값 구하기
# 부메랑은 항상 ㄱ 모양, 3칸 차지
# 중심부분이 강도 x 2배
# 부메랑 좌표.. 가운데를 중심으로
# (r, c-1), (r+1, c)
# (r, c-1), (r-1, c)
# (r-1, c), (r, c+1)
# (r, c+1), (r+1, c)

# print(arr)
# print(visited)


def back(r, c, strength):
    global ans

    # 반복/종료 조건
    if c == m:
        # c를 리셋, r+1해서 하나 올려서 다음줄 탐색
        back(r+1, 0, strength)
        return
    if r == n:
        ans = max(ans, strength)
        return

    # 반복
    if not visited[r][c]:
        if 0 <= c - 1 < m and 0 <= r + 1 < n and not visited[r+1][c] and not visited[r][c-1]:
            visited[r][c] = 1
            visited[r + 1][c] = 1
            visited[r][c - 1] = 1
            strength += (arr[r][c]*2) + arr[r+1][c] + arr[r][c-1]
            back(r, c+1, strength)
            visited[r][c] = 0
            visited[r + 1][c] = 0
            visited[r][c - 1] = 0
            strength -= (arr[r][c] * 2) + arr[r + 1][c] + arr[r][c - 1]
        if 0 <= c - 1 < m and 0 <= r - 1 < n and not visited[r-1][c] and not visited[r][c-1]:
            visited[r][c] = 1
            visited[r-1][c] = 1
            visited[r][c-1] = 1
            strength += (arr[r][c]*2) + arr[r-1][c] + arr[r][c-1]
            back(r, c + 1, strength)
            visited[r][c] = 0
            visited[r - 1][c] = 0
            visited[r][c - 1] = 0
            strength -= (arr[r][c] * 2) + arr[r - 1][c] + arr[r][c - 1]
        if 0 <= r - 1 < n and 0 <= c + 1 < m and not visited[r - 1][c] and not visited[r][c + 1]:
            visited[r][c] = 1
            visited[r - 1][c] = 1
            visited[r][c + 1] = 1
            strength += (arr[r][c]*2) + arr[r-1][c] + arr[r][c+1]
            back(r, c + 1, strength)
            visited[r][c] = 0
            visited[r - 1][c] = 0
            visited[r][c + 1] = 0
            strength -= (arr[r][c] * 2) + arr[r - 1][c] + arr[r][c + 1]
        if 0 <= r+1 < n and 0 <= c+1 < m and not visited[r+1][c] and not visited[r][c+1]:
            visited[r][c] = 1
            visited[r+1][c] = 1
            visited[r][c+1] = 1
            strength += (arr[r][c]*2) + arr[r+1][c] + arr[r][c+1]
            back(r, c + 1, strength)
            visited[r][c] = 0
            visited[r + 1][c] = 0
            visited[r][c + 1] = 0
            strength -= (arr[r][c] * 2) + arr[r + 1][c] + arr[r][c + 1]
    back(r, c+1, strength)


n, m = map(int, input().split())    # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

visited = [[0] * m for _ in range(n)]
back(0, 0, 0)
print(ans)
