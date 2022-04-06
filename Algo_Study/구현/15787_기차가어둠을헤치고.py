import sys
sys.stdin = open("input_15787.txt")

# 기차엔 20개의 일렬 좌석
# 1 i x : i번째 기차에(1 ≤ i ≤ N) x번째 좌석에(1 ≤ x ≤ 20) 사람을 태워라.
# 이미 사람이 타있다면 , 아무런 행동을 하지 않는다.

# 2 i x : i번째 기차에 x번째 좌석에 앉은 사람은 하차한다.
# 만약 아무도 그자리에 앉아있지 않았다면, 아무런 행동을 하지 않는다.

# 3 i : i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로간다.
# k번째 앉은 사람은 k+1번째로 이동하여 앉는다.
# 만약 20번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.

# 4 i : i번째 기차에 앉아있는 승객들이 모두 한칸씩 앞으로간다.
# k번째 앉은 사람은 k-1 번째 자리로 이동하여 앉는다.
# 만약 1번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.

# 같은 승객 기록이 있다면 해당 기차는 은하수 통과 불가
# N = 기차의 수 / M = 명령의 수

N, M = map(int, input().split())
train = [[0] * 20 for _ in range(N+1)]    # 기차 수 + 1 만큼 좌석 만들기
state = []  # 승객 기록용 list

for _ in range(M):
    command = list(map(int, input().split()))
    train_num = command[1]

    if command[0] == 1:
        train[train_num][command[2]-1] = 1

    elif command[0] == 2:
        train[train_num][command[2]-1] = 0

    elif command[0] == 3:   # 앞으로 이동
        train[train_num].insert(0, 0)   # (index, 넣는 숫자)
        train[train_num].pop()  # 하차시키기

    elif command[0] == 4:   # 뒤로 이동
        train[train_num].pop(0)
        train[train_num].append(0)  # 승객 하차시키기

cnt = 0
for i in range(1, N+1):
    if train[i] not in state:   # 똑같은 승객 수가 있는지 확인
        state.append(train[i])
        cnt += 1

print(cnt)