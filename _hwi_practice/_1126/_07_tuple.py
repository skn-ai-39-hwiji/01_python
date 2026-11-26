"""
tuple

- 바깥 요소 재대입을 허용하지 않는 불변 시퀀스이다.
- 저장순서 기억
- 주로 데이터의 집합을 안전하게 유지하거나, 함수에서 여러 값을 반환할 때 사용
- list는 바뀔 수 있는 목록, tuple은 구조가 고정된 값 묶음으로 설명할 수 있다.

- 예: 학생 정보처럼 계속 수정될 수 있으면 list, 
      RGB값처럼 고정된 묶음은 tuple
"""

print("--- tuple ---")


t1 = () # 빈 튜플
t2 = (10) # 값이 하나만 존재하는 튜플 == 일반 int로 해석
t3 = (10,) # [진짜] 값이 하나만 존재하는 튜플

print(f't1: {t1} - {type(t1)}') # t1: () - <class 'tuple'>
print(f't2: {t2} - {type(t2)}') # t2: 10 - <class 'int'>
print(f't3: {t3} - {type(t3)}') # t3: (10,) - <class 'tuple'>

t4 = (10, 20)
t5 = 10, 20  # 변수는 값 하나만 저장 가능 
             # -> 자동으로 tuple 하나로 묶음

print(f't4: {t4} - {type(t4)}') # t4: (10, 20) - <class 'tuple'>
print(f't5: {t5} - {type(t5)}') # t5: (10, 20) - <class 'tuple'>


print("--- tuple indexing ---")
tpl = ('a', 'b', 'c', 'd')
print('tpl[0]:', tpl[0])
print('tpl[1]:', tpl[1])

print("--- tuple slicing ---")
print('tpl[0:3]:', tpl[0:3]) 

"""tuple unpacking
- 묶여있는 값을 푸는 방법

- *튜플변수
"""

print("--- tuple unpacking ---")
# tpl = ('a', 'b', 'c', 'd')

# ('A', 'a', 'b', 'c', 'd') 만들기
tpl_ =  ('A',) + tpl
print("('A',) + tpl = ", tpl_)














