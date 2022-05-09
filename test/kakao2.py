# 각 큐의 원소의 합이 같게 만들기
# 이때 필요한 작업의 최소 횟수
# 한번 pop, insert를 합해서 1회로 봄
# 선입선출!!

def solution(queue1, queue2):
    count = 0
    target = int((sum(queue1) + sum(queue2)) / 2)   # 큐 2개 합이 홀수인것도 고려?
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    diff = abs(sum(queue1) - sum(queue2))
    print(diff, target, '\n합1:', sum1, '합2:', sum2)
    # 즉 큐1과 큐2에서 diff // 2만큼의 숫자만큼 큐1, 큐2에 더해야함
    # abs(큐1 - 큐2) == diff // 2 인 값을 찾아서 바꾸기

    for i in range(len(queue1)):
        for j in range(len(queue2)):
            if abs(diff - abs(queue1[i] - queue2[j])) <= 5: # 이 둘의 차이가 가깝다면
                print('가깝다', queue1[i], queue2[j])
                print(j)
            else:
                continue
    count = -1
    print('카운트', count)
    return count


# solution([3, 2, 7, 2], [4, 6, 5, 1]) 답 2
solution([1, 2, 1, 2], [1, 10, 1, 2])
# 답 7
# solution([1, 1], [1, 5]) 답 -1