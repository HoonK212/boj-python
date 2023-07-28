import sys; input = sys.stdin.readline
if __name__ == '__main__':

  for _ in range(3):
    yut = list(map(int, input().split()))
    print({0: 'E', 1: 'A', 2: 'B', 3: 'C', 4:'D'}.get(yut.count(0)))
