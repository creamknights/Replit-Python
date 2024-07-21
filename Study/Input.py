n = input()

n = int(input())

a, b = map(int, input().split())

array = list(map(int, input().split()))

#많은 양의 데이터를 빠르게 입력 받아야 할 때
import sys

n = sys.stdin.readline()
n = int(sys.stdin.readline())

# sys.stdin.readline()은 입력 문자열의 끝에 개행 문자(\n)를 포함하므로
# 이 개행 문자를 제거하려면 .rstrip() 메서드를 사용
n = sys.stdin.readline().rstrip()

# 백준 10952번, 0 0을 입력 받으면 종료
while True:
  a, b = map(int, input().split())
  if (a == 0 and b == 0):
    break
  else:
    print(a + b)

# 백준 10951번, 테스트 케이스의 개수가 정해지지 않은 경우 try-except
while True:
  try:
    a, b = map(int, input().split())
    print(a + b)
  except:
    break
