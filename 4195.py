import sys; input = sys.stdin.readline
from collections import deque
if __name__ == '__main__':

  def add(h1, h2):
    global friends_dict

    if h1 not in friends_dict.keys():
      friends_dict[h1] = [h2]
    elif h2 not in friends_dict[h1]:
      friends_dict[h1].append(h2)

  def count(h):
    global friends_dict

    queue = deque([friends_dict[h]])
    visited = [h]
    friends_network = [h]

    while queue:
      friends = queue.pop()

      for friend in friends:
        if friend not in visited:
          visited.append(friend)
          friends_network.append(friend)
          queue.append(friends_dict[friend])

    return len(friends_network)

  n = int(input())

  for _ in range(n):
    friends_dict = {}
    m = int(input())

    for _ in range(m):
      a, b = map(str, input().rstrip().split())
      add(a, b)
      add(b, a)
      print(count(a))
