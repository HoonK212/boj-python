import sys; input = sys.stdin.readline
if __name__ == '__main__':

  a, b, c = map(int, input().split())

  # 사칙연산 기호, 등호 순서인 경우
  if a + b == c:
    print(f"{a}+{b}={c}")
  elif a - b == c:
    print(f"{a}-{b}={c}")
  elif a * b == c:
    print(f"{a}*{b}={c}")
  elif a // b == c:
    print(f"{a}/{b}={c}")

  # 등호, 사칙연산 기호 순서인 경우
  elif a == b + c:
    print(f"{a}={b}+{c}")
  elif a == b - c:
    print(f"{a}={b}-{c}")
  elif a == b * c:
    print(f"{a}={b}*{c}")
  elif a == b // c:
    print(f"{a}={b}/{c}")
