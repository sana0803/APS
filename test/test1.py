# 새 마스크 착용일부터 이틀후까지만 재사용하고 폐기
# 단 미세/초미세 둘다 매우나쁨 상되면 그날만 씀


def solution(atmos):
    count = 0
    print(atmos)
    mask_day = -1

    for i in range(len(atmos)):
        print(atmos[i])
        if atmos[i][0] >= 151 and atmos[i][1] >= 76:    # 둘 다 매우나쁨 상태면
            if mask_day > -1:   # 개시한 마스크가 있다면
                mask_day = -1
            else:       # 사용중인 마스크 없다면 새로쓰기
                count += 1
                mask_day = -1
                print('갯수 17', count)

        elif atmos[i][0] >= 81 or atmos[i][1] >= 36:  # 둘중 하나라도 나쁨 이상이면
            if mask_day > -1:   # 개시한 마스크가 있다면
                mask_day += 1
                if mask_day == 2:   # 마스크쓴지 이틀째면 리셋
                    mask_day = -1
            else:
                count += 1
                mask_day += 1
                if mask_day == 2:
                    mask_day = -1
                print('갯수 30', count)
        # 공기 나쁜 상태는 아니지만 개시한 마스크가 있을때
        elif atmos[i][0] < 81 and atmos[i][1] < 36 and mask_day > -1:
            mask_day += 1
            if mask_day == 2:
                mask_day = -1
        print('마스크', mask_day)
    print('갯수', count)

    return count


solution([
    [80, 35],
    [70, 38],
    [100, 41],
    [75, 30],
    [160, 80],
    [77, 29],
    [181, 68],
    [151, 76],
  ])