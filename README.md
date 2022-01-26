## 21 06 24

### Programmers_Lv.1

- **List comprehension**
  - `[ㅁㅁㅁ for ㅁ in ㅁㅁㅁ] `
  - 앞 부분이 리스트에 추가할 각 요소
  - `[print(i,end=' ') for i in range(1,n+1) if n%i==0]` if문 섞은 활용
- **''.join()**
  - ![image-20210625140312703](C:\Users\new\AppData\Roaming\Typora\typora-user-images\image-20210625140312703.png)
  - list, str, tuple에서 사용 가능
  - 리스트나 str 요소들을 `''`기준으로 합쳐줌. 비워두면 defalt 값은 공백. 



## 21 06 25

### Programmers_Lv.1

- **삼항 연산자**
  - `ㅁㅁㅁ if ??? else ㅇㅇㅇ `
  - if ??? 가 참이면 ㅁㅁㅁ 실행, 거짓이면 ㅇㅇㅇ 실행
  - `a = 2 if k==3 else 4` : k == 3이 참이면 a=2, 거짓이면 a=4 / `else 4`는 `a = `이 생략. 원래 그렇게 작성하는 것!
- **set**
  - 중복을 불허, 입력 순서는 중요하지 않음
  - set 자료형은 만들때 `변수 = set()`을 통해 생성
  - 값을 추가하려면 `set.add()`
- **.find() 와 .index()**
  - find() 는 str에서 쓸수 있지만 list에서는 쓸 수 없다.

