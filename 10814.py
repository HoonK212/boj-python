import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  members = [tuple(map(str, input().rstrip().split())) for _ in range(n)]

  # case1: 260ms
  # members.sort(key=lambda x: int(x[0]))
  # for member in members:
  #   print(member[0], member[1])

  # case2: 252ms
  for member in sorted(members, key=lambda x: int(x[0])):
    print(member[0], member[1])
