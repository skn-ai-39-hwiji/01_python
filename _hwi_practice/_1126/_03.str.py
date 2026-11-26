""" 문자열(str)

- 문자가 나열된 형태
- 리터럴 표기법: " ", ' ', """ """, ''' ''' 

- 문자열은 문자들이 순서대로 나열된 텍스트 시퀀스이다.
- 문자의 순서는 0 부터 시작
- 이때, 시퀀스 순서를 index라고 부른다

- 문자열 전용 메서드가 제공된다
"""

s4 = '''1번줄
2번
3번줄
'''

s5 = """ aaa
bbb
vvv
"""

print(s4)
print(s5)

# + 연산자:  문자열 이어쓰기 

# len(문자열 또는 객체): 파이썬 객체(문자열, 리스트, 튜플, 딕셔너리, 셋...)
#                       의 길이(요소의 개수)를 반환하는 함수

text = "hello"
print("len(text):", len(text))

# str.replace(old, new) : 문자열 중 old를 찾아서 new로 변환
print('--- str.replace() ---')
today = '2026-11-25'
today_ = today.replace('-', '/')
print(today_)

# str.strip(문자열) : 문자열 시작/끝 부분 공백 제거
print("--- str.strip() ---")
text = '   hello   '
print(text.strip()) # hello
print(text.lstrip()) # hello   
print(text.rstrip()) #    hello

""" 
문자열(문자 + 배열)
- 파이썬의 문자열을 나타내는 str은 text sequence 형태를 갖는다.
- sequence: 순서가 있는 데이터 구조 (0-based index)
- 0-based index: 0부터 시작, 마지막 인덱스는 (길이-1)
- 인덱스를 통해 접근 가능
"""

print("--- 문자열 인덱싱 ---")
temp = "혼자 공부하는 파이썬"
print(temp[0],  temp[5], temp[10])
print( temp[len(temp) - 1] ) # 마지막 글자 찾기
print(len(temp))

print("--- slicing ---")
temp = "파이썬 머신러닝 판다스 데이터 분석"

print(temp[0:3]) # 파이썬
print(temp[4:8]) # 머신러닝

""" stop을 작성하지 않은 경우 == 끝까지 """
print(temp[9:]) # 판다스 데이터 분석
print(temp[-2:]) # 분석
print(temp[:9]) # 분석

