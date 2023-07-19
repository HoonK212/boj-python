import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def solution(num):
    for i in range(2, int(int(num) ** 0.5) + 1):
      if int(num) % i == 0:
        return

    if len(num) == n:
      print(num)
      return

    for suffix in suffix_list:
      solution(num + suffix)

  n = int(input())
  first_list = ['2', '3', '5', '7']
  suffix_list = ['1', '3', '7', '9']

  for first in first_list:
    solution(first)
