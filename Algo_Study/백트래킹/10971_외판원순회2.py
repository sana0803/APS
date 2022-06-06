import sys
sys.stdin = open("input_10971.txt")

# 도시의 수 N / N개의 줄에 비용행렬
# W[i][j] = 도시 i에서 도시 j로 가기 위한 비용
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 여행경로 짜기
# 순회 최소비용 구하기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
# print(arr)
cost = 99999999


def go(start, arrive, ans):   # 내 위치: start / 도착 도시: arrive / 비용 cost
    global cost, visited

    # 종료: ans가 cost 값보다 더 커지면 올 필요 x
    if ans > cost:
        return

    # 도시를 모두 방문했을때
    if sum(visited) == N:
        # print(arr[arrive][start])
        # 최종 도착 도시에서 처음 시작한 도시로 돌아가기때문에 가격 더하기
        # cost값 + 해서 비교하기, 갱신
        cost = min(cost, ans+arr[arrive][start])
        return

    # 반복
    for j in range(N):  # 다음 도착할 도시 찾기 for문
        # 갈 도시에 길이 있는지, 방문했는지 확인 / j != start 내 위치는 패스
        if arr[arrive][j] and j != start and not visited[j]:
            visited[j] = 1
            # print('36번 줄', visited, start)
            ans += arr[arrive][j]    # 값 더하기
            go(start, j, ans)  # 이 도시에 도착해 여기서 다시 길찾기 시작
            visited[j] = 0


for i in range(N):
    visited[i] = 1
    go(i, i, 0)     # 각각의 도시에서 시작
    visited[i] = 0

print(cost)