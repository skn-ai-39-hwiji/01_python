print("안녕하세요\n안녕하세요")

print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")

print(""" 동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라만세 """)
#문자선택 연산자 출력
print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print("안녕하세요"[4])
#반대로 출력
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
# slicing 지원
# - 문자열의 일부를 가져오는 방법
# - [start:stop:step]
# - start 시작하는 인덱스 (inclusive)
# - stop 종료 인덱스 (포함되지 않음. exclusive)
# - step 인덱스 이동 간격 (기본값 1)
print("안녕하세요"[1:4])

#문자열 길이
# len(문자열 또는 객체): 파이썬 객체(문자열, 리스트, 튜플, 딕셔너리, 셋...)
#                       의 길이(요소의 개수)를 반환하는 함수
print(len("안녕하세요"))


# f-string 
# - 작성법:  f"문자열 {변수}"  
# 변수 값을 문자열에 포함

print("[출력]")

a=5
b=3
print(a+b)


print("5+3=8")

print(a,"+",b ,"=",(a+b))
print(f"{a} + {b} = {a+b}")


name = input("이름을 입력하세요")
age = input("나이를 입력하세요")
print(f"{name}님은 {age}세 입니다.")
