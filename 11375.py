import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def dfs(employee):
    # 현재 직원이 할 수 있는 모든 일을 순회
    for task in tasks_per_employee[employee]:
      # 해당 일이 아직 다른 직원에게 할당되지 않았다면
      if not visited[task]:
        # 해당 일을 방문했다고 표시
        visited[task] = True
        # 해당 일이 아직 할당되지 않았거나, 이미 할당된 일이지만 그 일을 담당하는 다른 직원이 다른 일을 할 수 있다면
        if assigned_to[task] == -1 or dfs(assigned_to[task]):
          # 현재 직원을 이 일에 할당
          assigned_to[task] = employee
          # 일 할당 성공
          return True
    # 현재 직원이 할 수 있는 일 중 할당할 수 있는 일이 없음
    return False


  n, m = map(int, input().split())
  tasks_per_employee = [list(map(int, input().split()))[1:] for _ in range(n)]

  # 각 일을 담당하는 직원 번호 (-1은 아직 할당되지 않았음을 의미)
  assigned_to = [-1] * (m + 1)

  # 결과(할당된 일의 수) 초기화
  result = 0

  # 모든 직원에 대해 DFS를 실행하여 일 할당
  for employee in range(n):
    visited = [False] * (m + 1)
    # 현재 직원으로부터 시작하여 DFS 실행, 할당 가능한 일이 있다면 결과를 1 증가
    if dfs(employee):
      result += 1

  # 최대 할 수 있는 일의 개수 출력
  print(result)