import sys
sys.stdin = open("input.txt")

numbers = set(range(1, 10000))
# print(numbers)
remove_set = set()

for num in numbers: # 1, 2, 3, 4...
    for j in str(num): # 1
        num += int(j) # 1+=1
    remove_set.add(num) # set에는 add로 요소 추가(셀프넘버가 아닌 애들)

self_numbers = numbers - remove_set # 차집합 구하기
for self_num in sorted(self_numbers): # sorted하면 리스트로 반환
    print(self_num)

