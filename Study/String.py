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
print(result)  # 출력: abc

# (***) 리스트 요소가 문자열이 아닌 경우 TypeError 발생
# 리스트의 모든 요소를 문자열로 변환한 후에 join 사용
numbers = [1, 2, 3]
result = ' '.join(map(str, numbers))
print(result)  # 출력: 1 2 3

# 백준 10810번
n, m = map(int, input().split())  # 1번부터 n번이 적힌 n개의 바구니
array = [0] * n
for _ in range(m):
            i, j, k = map(int, input().split())
            # i번부터 j번 바구니에 k번이 적힌 공을 넣는다.
            array[i - 1:j] = [k] * (j - i + 1)
print(" ".join(map(str, array)))  # join() 메서드는 문자열에만 적용할 수 있으므로 문자열로 변환 후 사용
"""
replace
문자열 내의 특정 부분 문자열을 다른 문자열로 대체
대체된 새로운 문자열을 반환
"""
a = 'hello, world'
print(a.replace('hello', 'hi'))  # hi, world
print(a)  # hello, world
a = a.replace('hello', 'hi')
print(a)  # hi, world

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

# print() end 옵션
# end=' '로 설정하면 줄 바꿈 대신 공백을 출력
print("a", end=" ")
print("b")
# 출력: a b

print('a', 'b', 'c')  # a b c
print('a' + 'b' + 'c')  # abc

# 별 찍기2
n = int(input())
for i in range(1, n + 1):
            print(' ' * (n - i) + '*' * i)

# 아스키코드 출력
print(ord('A'))
# 숫자를 문자로 출력
print(chr(65))  # A
print(chr(ord('A')))

# 문자열을 정수 리스트로 변환
num_string = '12345'
array = list(''.join(map(str, num_string)))
print(array)  # ['1', '2', '3', '4', '5']
arr = list(map(int, array))
print(array)  # [1, 2, 3, 4, 5]

# 리스트 컴프리헨션을 사용하여 문자열을 정수 리스트로 변환 (백준 11720번)
num_string = '12345'
array = [int(char) for char in num_string]

print(array)  # [1, 2, 3, 4, 5]

# 백준 10809번, index() 메서드와 find 메서드
"""
index() 메서드는 특정 문자열에서 특정 문자의 인덱스를 반환
 특정 문자가 문자열에 존재하지 않으면 ValueError (예외 처리 필요)
find() 메서드는 특정 문자가 문자열에 존재하지 않으면 -1을 반환하는 차이점
"""
my_string = 'python'
print(my_string.index('p'))  # 0 (p가 위치하는 인덱스 반환)
print(my_string.find('p'))  # 0
print(my_string.find('a'))  # my_string에 'a'가 존재하지 않으므로 -1 반환

# 백준 10988번, 팰린드롬 확인하기
# 팰린드롬은 거꾸로 읽어도 같은 단어
word = 'level'
if word == word[::-1]:
            print(1)
else:
            print(0)

# (***) 백준 1316번, 그룹 단어의 개수 출력
# aba, aabba, abca 는 그룹 단어가 아니다
n = int(input())
count = n
for _ in range(n):
            word = input()
            for i in range(len(word) - 1):
                        if word[i] == word[i + 1]:
                                    pass
                        elif word[i] in word[i + 2:]:
                                    count -= 1
                                    break
print(count)
