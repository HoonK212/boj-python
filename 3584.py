import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  t = int(input())
  for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1)

    for _ in range(n - 1):
      i, j = map(int, input().split())
      parent[j] = i

    a, b = map(int, input().split())
    a_parents, b_parents = [0, a], [0, b]

    while parent[a]:
      a_parents.append(parent[a])
      a = parent[a]

    while parent[b]:
      b_parents.append(parent[b])
      b = parent[b]

    i = 1
    while a_parents[-i] == b_parents[-i]:
      i += 1

    print(a_parents[-i + 1])
