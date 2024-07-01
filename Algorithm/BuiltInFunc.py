""" 

파이썬에서 자주 사용되는 유용한 표준 라이브러리

내장 함수

itertools - 반복되는 형태의 데이터를 처리하기 위한 기능 제공
(***) 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용된다. (완전탐색 유형)

heapq - 힙(Heap) 자료구조 제공
 우선순위 큐 기능을 구현하기 위해 사용 (다익스트라 최단 경로 알고리즘)

bisect - 이진탐색 기능 제공

collections - 덱(deque), 카운터(Counter) 자료구조 포

math - 필수적인 수학적 기능 제공
 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, 파이(Pi)

"""

# 자주 사용되는 내장 함수

# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)  # 56

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)  # 튜플의 두 번째 원소가 정렬 기준
print(result)

# 순열과 조합
# 순열 nPr (Permutation)
# 조합 nCr (Combination)

from itertools import permutations

data = ['A', 'B', 'C']  # 데이터 준비

result = list(permutations(data, 3))  # 모든 순열 구하기 3P3
print(
    result
)  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))  # 3C2
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열과 중복 조합

from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))  # 중복 순열 3∏2
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))  # 중복 조합 3H2
print(result)

# Counter
"""

파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다.
리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려준다.

"""

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # blue가 등장한 횟수 출력
print(counter['green'])  # green이 등장한 횟수 출력
print(dict(counter))  # 사전 자료형으로 반환 {'red': 2, 'blue': 3, 'green': 1}

# 최대 공약수와 최소 공배수
# 최대 공약수 math 라이브러리의 gcd() 함수

import math


# 최소 공배수(LCM)을 구하는 함수 정의
def lcm(a, b):
  return a * b // math.gcd(a, b)  # 최대 공약수 필요


a = 21
b = 14

print(math.gcd(21, 14))  # 최대 공약수(GCD) 계산 7
print(lcm(21, 14))  # 최소 공배수 계산 42
