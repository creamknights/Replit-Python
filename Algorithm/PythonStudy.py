"""

파이썬 문법 정리
(이코테 2021) 이것이 취업을 위한 코딩 테스트다 with 파이썬 유투브 강의 기반

"""
import sys

a = 5.  # 5.0
a = -.7  # -0.7
a = 1e9  # 10의 9제곱(1,000,000,000)
print(a)  # 1000000000.0
a = int(1e9)
print(a)  #1000000000

a = 0.3 + 0.6
print(a)  # 0.8999999999999999
# 컴퓨터는 2진수 체계 연산을 수행하기 때문에 0.3과 0.6을 더한 값 0.9를 정확히 표현할 수 없다.

if a == 0.9:
  print(True)
else:
  print(False)  # False

# 표현상의 한계 해결을 위한 반올림 round()
a = 0.3 + 0.6
print(round(a, 4))  # 0.9

if round(a, 4) == 0.9:
  print(True)  # True
else:
  print(False)

# 수 자료형 연산
a = 7
b = 3

# 나누기(/)
# 파이썬에서 나누기 연산자(/)는 결과를 실수형으로 반환한다.
print(a / b)

# 나머지(%)
print(a % b)

# 몫(//)
print(a // b)

# 거듭 제곱(**)
print(a**b)

# 제곱근
print(a**0.5)
"""

# 리스트 자료형 (배열 혹은 테이블)
# 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형

"""

# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 네 번째 원소 값을 1로 변경
a[3] = 1
print(a[3])
# 인덱스 값으로 리스트의 특정 원소에 접근하는 것을 인덱싱(Indexing)이라고 한다.
# 음의 정수를 인덱스로 넣으면 원소를 거꾸로 탐색한다.

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 리스트에서 연속적인 위치의 원소들을 가져와야 할 때는 슬라이싱(Slicing)을 이용한다.
# [시작 인덱스 (이상) : 끝 인덱스 (미만)]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])  # 인덱스 1부터 인덱스 3까지 출력
"""

# 리스트 컴프리헨션
# 리스트를 초기화하는 방법 중 하나.
# 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화할 수 있다.

"""

# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)  # [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
odd_array = [i for i in range(20) if i % 2 == 1]
print(odd_array)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 일반적인 코드
array = []
for i in range(20):
  if i % 2 == 1:
    array.append(i)

print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
square_array = [i * i for i in range(1, 10)]
print(square_array)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

# 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있다.
# n x m 크기의 2차원 리스트를 한 번에 초기화해야 할 때 매우 유용하다.

"""

n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)
"""

# 4행 3열 2차원 리스트

[[0, 0, 0], 
 [0, 0, 0], 
 [0, 0, 0], 
 [0, 0, 0]]

"""

# 파이썬에서는 반복문에서 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.

# "Hello World" 5번 출력
for _ in range(5):
  print("Hello World")

# 1부터 9까지의 자연수를 더하기
summary = 0
for i in range(1, 10):
  summary += i
print(summary)  # 45
"""
리스트 관련 기타 메서드

append() - 리스트에 원소를 하나 삽입 - O(1)
sort() - 오름차순 정렬 - O(NlogN)
sort(reverse=True) - 내림차순 정렬 - O(NlogN)
reverse() - 리스트의 원소 순서 뒤집기 - O(N)
insert(삽입할 위치의 인덱스, 삽입할 값) - 리스트에 원소 삽입 - O(N)
count() - 특정한 값의 데이터의 개수 세기 - O(N)
remove() - 특정한 값의 데이터를 제거(여러 개면 하나만 제거) - O(N)

"""

a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)  # [1, 4, 3, 2]

a.sort()
print("오름차순 정렬: ", a)  # [1, 2, 3, 4]

a.sort(reverse=True)
print("내림차순 정렬: ", a)  # [4, 3, 2, 1]

print("값이 3인 데이터의 개수: ", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# 리스트에서 특정 값을 가지는 원소 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # 집합 자료형

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)  # [1, 2, 4]
"""

문자열 자료형

"""

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)
"""

문자열 연산 (+)
문자열 변수를 특정한 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러 번 더해진다.
문자열에 대해서도 인덱싱과 슬라이싱을 할 수 있다.
특정 인덱스의 값을 변경할 수는 없다.

"""

a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)  # StringStringString

a = "ABCDEF"
print(a[2:4])  # CD
"""

튜플 자료형
한 번 선언된 값을 변경할 수 ㅇ벗다.
리스트는 []를 사용하지만 튜플은 ()를 사용하면
튜플은 리스트에 비해 상대적으로 '공간 효율적'이다.

"""

# 튜플
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 네 번째 원소만 출력
print(a[3])  # 4

# 두 번째 원소부터 네 번째 원소까지 출력
print(a[1:4])  # (2, 3, 4)
"""

튜플을 사용하면 좋은 이유

서로 다른 성질의 데이터를 묶어서 관리해야 할 때
- 최단 경로 알고리즘에서는 (비용, 노드번호)의 형태로 튜플 자료형을 자주 사용한다.
데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
- 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
리스트보다 메모리를 효율적으로 사용해야 할 

"""
"""

사전 자료형

키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형
(리스트나 튜플은 값을 순차적으로 저장)
임의의 변경 불가능한 자료형을 키로 사용할 수 있다.
파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

"""

data = dict()
data['사과'] = 'Apple'  # key - 사과, value - Apple
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재한다.")
"""

사전 자료형 관련 메서드
키와 값을 별도로 뽑아내기 위한 메서드

keys() 함수 - 키 데이터만 뽑아서 리스트로 이용
values() 함수 - 값 데이터만 뽑아서 리스트로 이용

"""

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list)  # dict_keys(['사과', '바나나', '코코넛'])

# 값 데이터만 담은 리스트
value_list = data.values()
print(value_list)  # dict_values(['Apple', 'Banana', 'Coconut'])

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])

# 사전 자료형 초기화의 또다른 방법
b = {'사과': 100, '복숭아': 500}

print(b)  # {'사과': 100, '복숭아': 500}
print(b['사과'])  # 100

key_list = b.keys()
print(key_list)  # dict_keys(['사과', '복숭아'])

# 리스트 형태로 변환
key_list = list(b.keys())
print(key_list)  # ['사과', '복숭아']
"""

집합 자료형
- 중복을 허용하지 않는다.
- 순서가 없다.

데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

"""

# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)  # {1, 2, 3, 4, 5}

# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)  # {1, 2, 3, 4, 5}

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)

data = set([1, 2, 3])
print(data)  # {1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data)  # {1, 2, 3, 4}

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)  # {1, 2, 3, 4, 5, 6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)  # {1, 2, 4, 5, 6}
"""

리스트와 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.

사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다. 사전의 key, 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.

"""

# 기본 입출력
"""

자주 사용되는 표준 입력 방법

input() - 한 줄의 문자열을 입력 받는 함수
map() - 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용하는 함수
 ex) 공백을 기준으로 구분된 데이터를 입력 받을 때
   - list(map(int, input().split())) # 입력 받은 데이터를 공백을 기준으로 구분하고 정수형으로 바꿔준 다음 리스트에 저장
 ex) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다.
   - a, b, c = map(int, input().split())

"""

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여  입력
data = input().split()  # ['1', '2', '3', '4', '5']
""" 코딩 테스트에서 많이 활용 """
# data = list(map(int, input().split()))  # 정수형으로 저장 [1, 2, 3, 4, 5]

data.sort(reverse=True)  # 내림차순 정렬
print(data)
"""

최대한 빠르게 입력 받기
import sys
sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용한다.
단, 입력 후 Enter가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용한다.

입력의 개수가 많은 문제에서 사용한다.
이진 탐색, 정렬, 그래프 관련 문제에서 자주 사용된다.

"""

# 문자열 입력 받기
# data = sys.stdin.readline().rstrip()
# print(data)
"""

표준 출력 방법
기본 출력은 print() 함수를 이용한다.
print(a, b, c)
print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다. 줄 바꿈을 원치 않는 경우 end 속성을 이용한다.

"""

a = 1
b = 2
print(a, b)
print(7, end=" ")  # 줄 바꿈 되지 않는다.
print(8, end=" ")

answer = 7
print("정답은 " + str(answer) +
      "입니다.")  # 파이썬은 문자열과 정수형에 대해서 직접적인 + 연산을 수행할 수 없기 때문에 정수형을 문자열로 바꿔준다.

# f-string
answer = 7
print(f"정답은 {answer}입니다.")
""" 조건문 """

x = 15
if x >= 10:
  print("x >= 10")
elif x >= 5:
  print("x >= 5")
else:
  print("x < 5")
""" 

들여쓰기
파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정한다.


"""
""" 

조건문의 기본 형태
if ~ elif ~ else


"""
""" 

논리 연산자 (파이썬은 직관적)
X and Y (다른 언어에서의 &&)
X or Y
not X


"""

if True or False:
  print("Yes")

a = 15
if a <= 20 and a >= 0:
  print("Yes")

# 파이썬의 기타 연산자

# 파이썬의 pass 키워드 (나중에 작성할 코드)

a = 50
if a >= 30:
  pass
else:
  print("a < 30")

# 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.
x = 15
if 0 < x < 20:
  print("x는 0이상 20 미만의 수입니다.")

# 반복문

i = 1
result = 0

while i <= 9:
  result += i
  i += 1

print(result)

# 1부터 9까지 홀수의 합 구하기
i = 1
result = 0
while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)

# 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인한다. (무한 루프 주의)
""" 

for문

for 변수 in 리스트: # 리스트에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 방문한다.
  실행할 소스코드

"""

array = [9, 8, 7, 6, 5]
array = (1, 2, 3, 4, 5)

for x in array:
  print(x)
""" 

range()

for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용한다.
range(시작 값, 끝 값+1) 형태로 사용한다.
range(n)은 0부터 n-1까지의 정수를 순회한다.

"""

# continue
# 반복문에서 남은 코드의 실행을 건너뛰고 다음 반복을 진행하고자 할 때 사용한다.

result = 0

for i in range(1, 10):
  if i % 2 == 0:  # 짝수는 건너뛰고 홀수만 더한다.
    continue
  result += i

print(result)

# break
# 반복문을 즉시 탈출하고자 할 때 사용한다.

i = 1

while True:
  print("현재 i의 값:", i)
  if i == 5:
    break
  i += 1

# 합격 여부 판단 예제 1
# 점수가 80점을 넘으면 합격
scores = [90, 85, 77, 65, 97]

for i in scores:  # (*) i는 scores의 원소(값)을 의미한다. 90, 85, 77, 65, 97
  if i >= 80:
    print(f"{i+1}점은 80점 이상으로 합격입니다.")

for i in range(5):  # i는 0, 1, 2, 3, 4
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

for index, score in enumerate(scores):
  if score >= 80:
    print(i + 1, "번 학생은", score, "점으로 합격입니다.")  # 1번 학생은 90점으로 합격입니다.

# 합격 여부 판단 예제 2
# 특정 번호의 학생은 제외
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
  if i + 1 in cheating_student_list:
    continue
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

# 중첩된 반복문
for i in range(2, 10):
  for j in range(1, 10):
    print(i, "X", j, "=", i * j)
  print()  # 줄 바꿈
""" 함수

1. 내장 함수 - 파이썬이 기본적으로 제공하는 함수
2. 사용자 정의 함수
    def 함수명(매개변수):
        실행할 소스코드
        return 반환 

"""


def add(a, b):
  return a + b


print("함수의 결과", add(3, 7))  # 10
result = add(3, 7)
print(result)


def substract(a, b):
  print("함수의 결과", a - b)


# 파라미터의 변수를 직접 지정 가능 (순서 상관 없음)
substract(b=3, a=7)

# global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조한다.

a = 10


def func():
  global a
  a += 1


for i in range(10):
  func()

print(a)  # 20

# 전역 변수로 선언된 리스트 객체의 내부 메서드를 호출하는 것이 가능하다.
arr = [1, 2, 3, 4, 5]


def arr_func():
  arr.append(6)
  print(arr)


arr_func()  # [1, 2, 3, 4, 5, 6]

# 만약 함수 안에 전역 변수와 이름이 동일한 array = [3, 4, 5]가 존재한다면 함수 내부에 선언된 변수를 참조한다.

array = [1, 2, 3, 4, 5]


def array_func():
  array = [3, 4, 5]
  array.append(6)
  print(array)  # 함수 안의 array를 참조


array_func()  # [3, 4, 5, 6]
print(array)  # [1, 2, 3, 4, 5]

# global 키워드 사용
array = [1, 2, 3, 4, 5]


def global_array_func():
  global array  # (*) 전역 변수를 참조 [1, 2, 3, 4, 5]
  array = [3, 4, 5]  # 전역 변수 array [1, 2, 3, 4, 5]가 [3, 4, 5]로 변경
  array.append(6)  # [3, 4, 5, 6]
  print(array)  # [3, 4, 5, 6]


global_array_func()  # [3, 4, 5, 6]
print(array)  # [3, 4, 5, 6] (전역 변수의 array)


# 파이썬은 여러 개의 값을 한꺼번에 반환할 수 있다.
def operator(a, b):
  add_var = a + b
  sub_var = a - b
  mul_var = a * b
  div_var = a / b
  return add_var, sub_var, mul_var, div_var


a, b, c, d = operator(7, 3)
print(a, b, c, d)

# 람다 표현식
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다.

print((lambda a, b: a + b)(3, 7))  # add(3,7)과 동일

# 람다 표현식 예시 1
# 정렬에서 많이 사용된다.

# 모든 원소들이 튜플 형태로 존재하는 리스트
array = [('사과', 100), ('복숭아', 500), ('바나나', 200)]


def my_key(x):
  return x[1]  # 튜플의 두 번째 원소 반환


# 점수대로 오름차순 정렬 결과 출
print(sorted(array, key=my_key))  # [('사과', 100), ('바나나', 200), ('복숭아', 500)]
print(sorted(array, key=lambda x: x[1]))

#  람다 표현식 예시 2
# 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
# map은 각각의 원소에 접근
# 두 리스트의 같은 원소끼리 덧셈 연산

print(list(result))  # [7, 9, 11, 13, 15]
