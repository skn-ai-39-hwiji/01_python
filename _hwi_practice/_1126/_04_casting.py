print('1+2.3 =',1+2.3)

print(int('3') + 4) 

print(3, float(3), float('3'))

print('1'+ str(2))
print('bool(100):', 100, bool(100))
print('bool(-100):', -100, bool(-100))
print("bool('abcd'):", 'abcd', bool('abcd'))
print("bool(' '):", ' ', bool(' ')) # 공백 문자

print("bool({'is_friday': True}):", {'is_friday': True}, bool({'is_friday': True}))

print("--- bool() 형변환 - Falsy ---")
print("bool(0):", '', bool(0))
print('bool(0.0):', 0.0, bool(0.0))
print("bool(''):", '', bool('')) # 빈 문자열
print('bool([]):', [], bool([])) # 빈 리스트
print('bool(()):', (), bool(())) # 빈 튜플
print('bool({}):', {}, bool({})) # 빈 딕셔너리
print('bool(None):', None, bool(None))

# [A] if 조건식 else [B]

age= 19
print("성인" if age >=20 else "성인x")

s1 = ''

print('내용 0' if len(s1)>0 else '내용x')
print('내용 0' if bool(s1)>0 else '내용x')
print('내용 0' if s1  else '내용x')