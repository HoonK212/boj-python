import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(target):
    global parent_nodes

    # 삭제 대상인 노드를 -2로 표기
    parent_nodes[target] = -2

    for node, parent in enumerate(parent_nodes):
      # 부모 노드가 삭제 대상 노드인 경우, 자식 노드도 삭제 대상으로 표기
      if parent == target:
        dfs(node)

  n = int(input())
  parent_nodes = list(map(int, input().split()))
  remove_target = int(input())

  dfs(remove_target)

  answer = 0
  for node, parent in enumerate(parent_nodes):
    # 삭제 대상이 아니면서, 자식 노드가 없는 경우에 'answer += 1' 수행
    if parent != -2 and node not in parent_nodes:
        answer += 1

  print(answer)
