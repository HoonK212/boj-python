import sys; input = sys.stdin.readline;
if __name__ == '__main__':

  n, m = map(int, input().split())
  truth_list = set(input().split()[1:])
  parties = []

  for _ in range(m):
    parties.append(set(input().split()[1:]))

  for _ in range(m):
    for party in parties:
      # & -> 교집합 연산 (intersection)
      if party & truth_list:
        # | -> 합집합 연산 (union)
        truth_list = truth_list | party

  cnt = 0
  for party in parties:
    if party & truth_list:
      continue
    cnt += 1

  print(cnt)
