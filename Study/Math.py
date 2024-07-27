# B진법 수 N을 10진법으로 출력하기 (백준 2745번)
n, b = 'ZZZZZ', 36
print(int(n, b))  # 60466175
""" 36진법 ABC를 10진법으로 변환하기
A: 10, B: 11, C: 12
value = (12) * 36^0 + (11) * 36^1 + (10) * 36^2
"""
n, b = 'ABC', 36
n = n[::-1]  # 계산의 편의를 위해 'CBA'로 변환
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value = 0
for i, x in enumerate(n):
  value += array.index(x) * (b**i)
print(value)  # 13368

# 10진법 수 N을 B진법으로 변환하기 (백준 11005번)
n, b = 60466175, 36
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''
while n:
  result = array[n % b] + result  # 나중에 나누는 게 앞에 위치
  n //= b
print(result)  # ZZZZZ

# 삼각형 결정 조건 (백준 5073번)
# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 더 커야 한다.
array = [3, 2, 5]
if max(array) < sum(array) - max(array):
  print('Yes')
