import sys
sys.stdin = open("input_10971.txt")

# 도시의 수 N / N개의 줄에 비용행렬
# W[i][j] = 도시 i에서 도시 j로 가기 위한 비용
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 여행경로 짜기
# 순회 최소비용 구하기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N+1)
print(arr, visited)
cost = 99999

def go(start, j, cost):   # 내 위치 : start / 다음 도시: j
    global cost
    # 종료

    # 다음 도착할 도시 찾기 for문
    #     for 어쩌구 하기

    # 반복
    # 길이 있는지, 방문했는지 확인
    if arr[start][j] != 0 and not visited[j]:
        visited[start][j] = 1
        # cost가 값보다 더 커지면 올 필요 x / cost 값 + 해서 비교하기, 갱신

        # go(start=j, ?(모든 도시), cost)
        # for문 돌면서
        visited[start][j] = 0


go(0, 0, cost)