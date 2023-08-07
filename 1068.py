import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n = int(input())
  parent_list = list(map(int, input().split()))
  remove_node = int(input())

  def dfs(node, arr):
    arr[node] = -2
    for i, a in enumerate(arr):
      if a == node:
        dfs(i, arr)

  dfs(remove_node, parent_list)

  answer = 0
  for idx, parent in enumerate(parent_list):
    if parent != -2:
      if idx not in parent_list:
        answer += 1

  print(answer)
