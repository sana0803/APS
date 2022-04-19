# 말버릇 패턴 삭제 / 말버릇 패턴 : 길이가 1 이상인 패턴

def solution(call):
    call = call.lower()  # 대소문자 구분하지 않으므로 모두 소문자화
    word = []
    while len(call)
    for i in range(len(call)):
        word.append(call[i])

    print(word)


solution('abcabcdefabc')
