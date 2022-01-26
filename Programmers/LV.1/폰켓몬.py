def solution(nums):
    # 포켓몬 배열 nums / len = N
    # 가져갈 포켓몬 N/2마리
    # 가장 많은 종류의 포켓몬을 선택하는 방법의 포켓몬 종류 가짓수
    pick = set()
    cnt = len(nums) / 2  # 내가 가져갈 수 있는 폰켓몬 수

    for i in nums:
        pick.add(i)

    return cnt if cnt < len(pick) else len(pick)