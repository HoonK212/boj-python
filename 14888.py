import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
from itertools import permutations
if __name__ == '__main__':

  def calculate(n1, n2, s):
    if s == "+":
      return n1 + n2
    elif s == "-":
      return n1 - n2
    elif s == "*":
      return n1 * n2
    elif s == "//":
      if n1 >= 0:
        return n1 // n2
      else:
        return -(-n1 // n2)


  n = int(input())
  nums = list(map(int, input().split()))
  symbol_cnt = list(map(int, input().split()))
  symbol = ["+", "-", "*", "//"]

  symbols = []
  for i in range(4):
    if (symbol_cnt[i]) != 0:
      for _ in range(symbol_cnt[i]):
        symbols.append(symbol[i])

  per_list = list(permutations(symbols, n - 1))

  result, max, min = 0, 0, 0
  for i, per in enumerate(per_list):
    for j, s in enumerate(per):
      if j == 0:
        result = nums[j]
      result = calculate(result, nums[j + 1], s)

    if i == 0:
      max, min = result, result
    else:
      if result > max:
        max = result
      elif result < min:
        min = result

  print(max, min, sep='\n')
