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
"""
replace
문자열 내의 특정 부분 문자열을 다른 문자열로 대체
대체된 새로운 문자열을 반환
"""

a = 'nice to meet you'
# 모음 a, e, i, o, u 제거
result = a.replace("a",
                   "").replace("e",
                               "").replace("i",
                                           "").replace("o",
                                                       "").replace("u", "")
print(result)  # nc t mt y

# 정규 표현식으로 모음 a, e, i, o, u 제거
import re

a = 'nice to meet you'
# 정규 표현식을 사용하여 모음 제거
result = re.sub(r'[aeiou]', '', a)  # 문자열에서 a, e, i, o, u 중 하나라도 일치하는 부분을 찾음
print(result)  # nc t mt y

# 고양이 출력하기
print('\\    /\\')  # 백슬래쉬 \ 출력을 위해 앞에 \ 붙여줌
print(" )  ( ')")  # 작은 따옴표 출력을 위해 큰 따옴표로 감싸줌
print('(  /  )')
print(" \\(__)|")

# print() end
# end=' '로 설정하면 줄 바꿈 대신 공백을 출력
print("a", end=" ")
print("b")
# 출력: a b
