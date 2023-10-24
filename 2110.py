import sys; input = sys.stdin.readline
if __name__ == '__main__':

  def binary_search(arr):
    l = 1  # '가장 인접한 두 공유기 사이의 거리'의 최소값
    r = arr[-1] - arr[0]  # '가장 인접한 두 공유기 사이의 거리'의 최대값
    ans = 0

    while l <= r:
      m = (l + r) // 2  # binary search 구현을 위한 left, mid, right 설정
      p = arr[0]  # current point
      cnt = 1  # 공유기 수

      for i in range(1, n):
        if arr[i] >= m + p:
          p = arr[i]
          cnt += 1

      if cnt >= c:  # cnt가 c보다 크거나 같으면 left 증가시키기
        ans = m  # 해당 시점의 mid 값으로 answer 초기화
        l = m + 1
      else:  # cnt가 c보다 작으면 right 감소시키기
        r = m - 1

    return ans  # 최종 검색된 mid 값으로 반환


  n, c = map(int, input().split())
  x_list = list(int(input()) for _ in range(n))

  print(binary_search(sorted(x_list)))
