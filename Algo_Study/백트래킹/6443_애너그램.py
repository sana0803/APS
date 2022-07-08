import sys
sys.stdin = open("input_6443.txt")
# 입력받은 영단어의 철자로 만들수있는 모든 단어 출력하기 (알파벳 순서로)

ans = []
res = set()

def anagram(idx):
    global ans, res

    # 종료조건
    if len(ans) == len(alphabet):
        print(' '.join(map(str, ans)))
        return
        # tmp = ' '.join(map(str, ans))
        # if tmp not in res:
        #     res.append(tmp)
        # return res

    # 반복
    for i in range(len(alphabet)):
        if not visited[i]:
            ans.append(alphabet[i])
            visited[i] = 1
            anagram(idx + 1)
            ans.pop()
            visited[i] = 0


n = int(input())

for _ in range(n):
    alphabet = list(sorted(input()))
    visited = [0] * len(alphabet)
    # print(alphabet, visited)
    anagram(0)

for j in res:
    print(j)