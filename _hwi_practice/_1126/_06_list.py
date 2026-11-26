""" list

- 컨테이너(묶다)형 자료형이자 시퀀스(순서,index) 자료형

- 여러 값(lieral)을 묶어서 관리

- list에 값이 저장된 순서(index)를 기억한다.

- 같은 시퀀스 자료형으로 str, tuple이 있다.
"""

print("--- list ---")
lst = [10, 20, 30]

print(f'lst: {lst} - {type(lst)}')

print(f'lst[0]: {lst[0]} - {type(lst[0])}')

print("--- list 요소 추가/삭제  ---")
"""
- list는 값을 추가하거나 삭제할 수 있는 
  mutable 자료형이다.

- mutable 자료형: list, set, dict
- immutable 자료형: int, float, bool, str, tuple
"""

lst = [1,2,3,4]

print(id(lst)) #id() 함수 : 변수에 저장된 값의 식별코드 반환
before_id = id(lst)
lst.append(5)

after_id = id(lst)

print(lst, id(lst)) # 5 추가 확인, id 유지 확인
print(before_id == after_id) # 이전, 현재 id 비교


print("--- list insert ---")
# 리스트 내부 원하는 위치(index)에 요소 삽입(추가)
lst.insert(0, 0.5)
print("insert 후 lst:", lst)

lst.insert(3, 100)
print("insert 후 lst:", lst)

lst.insert(7, 777) # 제일 끝
print("insert 후 lst:", lst)

lst.insert(10, 999) # 중간에 인덱스 건너 뛰고 삽입
print("insert 후 lst:", lst) # -> 제일 끝에 삽입

print("--- list update ---")
lst2 = [100, 200, 300]

lst2[1] = 2
print("변경후 lst2 : " , lst2)


lst3 = ['aa','bb','cc','dd','ee','ff']

lst3.remove('bb')
print('remove 후 lst3:' , lst3)

lst4 = [10, 20, 30, 40]
removed = lst4.pop(1)
print("pop 수행 후 lst4:", lst4)
print("removed:", removed)


plates = ['plate1', 'plate2']

plates.append('plate3')
plates.append('plate4')

print(plates)    # ['plate1', 'plate2', 'plate3', 'plate4']

print(plates.pop())
print(plates)
print(plates.pop())
print(plates.pop())
print(plates)


""" 다차원 list
- list의 요소로 list가 존재하는 형태

* 2차원 list
- 1차원 list를 요소로 갖는 list
"""
lst6 = [1,2,3]  # 1차원
lst7 = [4,5,6]  # 1차원