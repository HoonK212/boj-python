import sys; input = sys.stdin.readline
if __name__ == '__main__':

  def getMinMax(i, j):
    global operations
    global answer

    tmp = []
    for mid in range(i, j):

      print("mid: ", mid)
      print("operations[mid]: ", operations[mid])
      print("answer[i][mid]: ", answer[i][mid])
      print("answer[mid + 1][j]: ", answer[mid + 1][j])

      if operations[mid] == '+':
        tmp.append(answer[i][mid][0] + answer[mid + 1][j][0])
        tmp.append(answer[i][mid][0] + answer[mid + 1][j][1])
        tmp.append(answer[i][mid][1] + answer[mid + 1][j][0])
        tmp.append(answer[i][mid][1] + answer[mid + 1][j][1])
      elif operations[mid] == '-':
        tmp.append(answer[i][mid][0] - answer[mid + 1][j][0])
        tmp.append(answer[i][mid][0] - answer[mid + 1][j][1])
        tmp.append(answer[i][mid][1] - answer[mid + 1][j][0])
        tmp.append(answer[i][mid][1] - answer[mid + 1][j][1])
      else:
        tmp.append(answer[i][mid][0] * answer[mid + 1][j][0])
        tmp.append(answer[i][mid][0] * answer[mid + 1][j][1])
        tmp.append(answer[i][mid][1] * answer[mid + 1][j][0])
        tmp.append(answer[i][mid][1] * answer[mid + 1][j][1])

      print("tmp: ", tmp)
      print("min(tmp): ", min(tmp))
      print("max(tmp): ", max(tmp))

    return min(tmp), max(tmp)

  n = int(input())
  expression = str(input()).rstrip()

  numbers = []
  operations = []

  # 숫자와 연산자 구분
  number_flag = True
  for char in expression:
    if number_flag:
      numbers.append(int(char))
      number_flag = False
    else:
      operations.append(char)
      number_flag = True

  oper_len = len(operations)
  answer = [[[0, 0] for _ in range(oper_len + 1)] for _ in range(oper_len + 1)]

  for scope in range(oper_len + 1):
    for i in range(oper_len + 1 - scope):
      j = i + scope

      print()
      print("i: ", i)
      print("j: ", j)

      if i == j:
        answer[i][j][0] = numbers[i]
        answer[i][j][1] = numbers[i]
      else:
        # 이전 min 값의 조합이 max 값이 될 수도 있기에 (ex: 음수와 음수의 곱)
        #   min과 max를 모두 저장하는 것이 핵심 !!!
        minTmp, maxTmp = getMinMax(i, j)
        answer[i][j][0] = minTmp
        answer[i][j][1] = maxTmp

      for a in answer:
        print(a)

  print(max(answer[0][oper_len]))
