import sys
sys.stdin = open("input_5209.txt")

# 제품 N종을 N곳의 공장에서 한곳당 한가지씩 생산
# 각 제품의 공장별 생산비용을 보고 전체 제품의 최소 생산비용 구하기
T = int(input())


def backtrack(min_cost, idx):   # idx 번째 제품의 최소가격을 체크
    global ans

    # 가지 치기
    if min_cost >= ans:  # 최소값이 이미 구한값보다 크면 종료. 이거 안하면 답틀림
        return

    # 종료 조건
    if idx == N:    # 검사 다 했으면
        ans = min_cost
        return

    # 백트래킹
    for i in range(N):  # 첫번째 제품의 i번째 가격을 체크하는것
        if not visited[i]:  # 방문 안했다면
            visited[i] = 1  # 방문체크 후 다음 idx 값 살펴보고 오기
            print(visited)
            backtrack(min_cost+arr[idx][i], idx+1)
            visited[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]  # 방문기록
    ans = 100 * N
    print(arr)
    backtrack(0, 0)

    print('#{} {}'.format(tc, ans))