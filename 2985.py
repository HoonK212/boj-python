import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  a, b, c = map(int, input().split())
  if a + b == c:
    print(f"{a}+{b}={c}")
  elif a - b == c:
    print(f"{a}-{b}={c}")
  elif a * b == c:
    print(f"{a}*{b}={c}")
  elif a // b == c:
    print(f"{a}/{b}={c}")
  elif a == b + c:
    print(f"{a}={b}+{c}")
  elif a == b - c:
    print(f"{a}={b}-{c}")
  elif a == b * c:
    print(f"{a}={b}*{c}")
  elif a == b // c:
    print(f"{a}={b}/{c}")
