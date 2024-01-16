import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  n, m = map(int, input().split())

  arr_a = []
  arr_b = []

  # n * m 크기의 a행렬 초기화
  for _ in range(n):
    arr_a.append(list(map(int, input().split())))

  # n * m 크기의 b행렬 초기화
  for _ in range(n):
    arr_b.append(list(map(int, input().split())))

  for i in range(n):
    for j in range(m):
      print(arr_a[i][j] + arr_b[i][j], end=' ') # 행 순서대로 행렬의 곱 계산
    print()
