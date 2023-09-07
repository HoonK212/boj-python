import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())
  scores = [list(map(str, input().rstrip().split())) for _ in range(n)]

  # 인덱스의 순서와 부호에 유의하여 sort 실행
  scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

  for score in scores:
    print(score[0])
  