import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
# from collections import deque
if __name__ == '__main__':

  # 두 노드를 연결하는 함수
  def union(a, b):
    a = find(a)
    b = find(b)

    if a != b: # 루트 노드가 다르면
      parents[b] = a # b의 루트를 a의 루트로 변경하고
      visited[a] += visited[b] # a의 루트 노드가 가진 친구 수에 b의 루트 노드가 가진 친구 수를 더하는 것이 핵심 !!!

  # 루트 노드 검색 함수
  def find(a):
    if parents[a] != a:
      parents[a] = find(parents[a])

    return parents[a]

  n = int(input())

  for _ in range(n):
    parents = {}
    visited = {}

    m = int(input())

    for _ in range(m):
      a, b = input().split()

      if a not in parents: # a나 b가 parents 딕셔너리에 없다면
        parents[a] = a # 각자 자신을 부모로 갖고
        visited[a] = 1 # 친구 수는 1로 설정

      if b not in parents:
        parents[b] = b
        visited[b] = 1

      union(a, b)

      print(visited[find(a)])

  # def add(h1, h2):
  #   global friends_dict
  #
  #   if h1 not in friends_dict.keys():
  #     friends_dict[h1] = [h2]
  #   elif h2 not in friends_dict[h1]:
  #     friends_dict[h1].append(h2)
  #
  # def count(h):
  #   global friends_dict
  #
  #   queue = deque([friends_dict[h]])
  #   visited = [h]
  #   friends_network = [h]
  #
  #   while queue:
  #     friends = queue.pop()
  #
  #     for friend in friends:
  #       if friend not in visited:
  #         visited.append(friend)
  #         friends_network.append(friend)
  #         queue.append(friends_dict[friend])
  #
  #   return len(friends_network)
  #
  # n = int(input())
  #
  # for _ in range(n):
  #   friends_dict = {}
  #   m = int(input())
  #
  #   for _ in range(m):
  #     a, b = map(str, input().rstrip().split())
  #     add(a, b)
  #     add(b, a)
  #     print(count(a))
