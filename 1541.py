import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  arr = input().split('-')

  num = []
  for i in arr:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
      sum += int(j)
    num.append(sum)

  n = num[0]
  for i in range(1, len(num)):
    n -= num[i]

  print(n)
