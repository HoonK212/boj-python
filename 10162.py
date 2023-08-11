import sys; input = sys.stdin.readline
if __name__ == '__main__':

  # 10162

  a = int(300)
  b = int(60)
  c = int(10)
  t = int(input())

  if t % c == 0:
    x = t // a
    y = (t % a) // b
    z = (t % b) // c
    print(x, y, z)
  else:
    print(-1)
