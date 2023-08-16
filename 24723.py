import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())

  # 1 1 / 2
  # 1 2 1 / 4
  # 1 3 3 1 / 8
  # 1 4 6 4 1 / 16
  # 1 5 10 10 5 1 / 32
  # 1 6 15 20 15 6 1 / 64

  print(2**n)
