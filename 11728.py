import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  input()
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  answer = A + B
  answer.sort()
  print(*answer)
