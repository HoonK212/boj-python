import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
if __name__ == '__main__':

  def generate_cantor_set(length):
    # 길이가 1인 경우 "-"
    if length == 1:
      return "-"

    # 3등분해서 재귀 처리
    third = length // 3
    left_part = generate_cantor_set(third)  # 왼쪽 부분
    center_part = " " * third  # 가운데 부분 (공백)
    right_part = generate_cantor_set(third)  # 오른쪽 부분

    return left_part + center_part + right_part

  while True:
    try:
      n = int(input())
      length = 3 ** n # 길이 = 3의 n제곱
      result = generate_cantor_set(length)
      print(result)
    except:
      break