import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  titles = {}

  for _ in range(n):
    title = str(input().rstrip())

    if title in titles.keys():
      titles[title] += 1
    else:
      titles[title] = 1

  # 가장 많이 팔린 책이 여러 개일 경우, 사전 순으로 가장 앞서는 제목을 출력하기 위해 다중 인자를 활용하여 익명 함수 사용
  sorted_titles = sorted(titles.items(), key = lambda item : (-item[1], item[0]))
  print(sorted_titles[0][0])
