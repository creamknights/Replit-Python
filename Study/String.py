# 슬라이싱을 이용한 문자열 뒤집기
a = '문자열뒤집기'
print(a[::-1])  # 기집뒤열자문
"""
join
문자열의 리스트를 하나의 문자열로 결
separator.join(iterable)

"""

a = ['a', 'b', 'c']
result = ', '.join(a)
print(result)  # 출력: a, b, c

# 빈 문자열을 구분자로 사용
a = ['a', 'b', 'c']
result = ''.join(a)
print(result)  # 출력: Hello

# 리스트 요소가 문자열이 아닌 경우 TypeError 발생
# 리스트의 모든 요소를 문자열로 변환한 후에 join 사용
numbers = [1, 2, 3]
result = ', '.join(map(str, numbers))
print(result)
# 출력: 1, 2, 3
