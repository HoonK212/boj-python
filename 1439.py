import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  s = input().rstrip()
  cnt = 0
  for i in range(len(s) - 1):
      if s[i] != s[i+1]:
          cnt += 1
  print((cnt + 1) // 2)
