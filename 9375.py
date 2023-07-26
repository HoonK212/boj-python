import sys; input = sys.stdin.readline
if __name__ == '__main__':

  n = int(input())

  for _ in range(n):
    cnt = int(input())

    # category_list = []
    # clothes_cnt_list = []

    clothes = {}

    # for _ in range(cnt):
    #   name, category = input().split()
    #
    #   if category in category_list:
    #     i = category_list.index(category)
    #     clothes_cnt_list[i] += 1
    #   else:
    #     category_list.append(category)
    #     clothes_cnt_list.append(1)

    for _ in range(cnt):
        name, category = input().split()

        if category in clothes.keys():
            clothes[category] += 1
        else:
          clothes[category] = 1

    # answer = 1
    # for cnt in clothes_cnt_list:
    #   answer *= cnt + 1

    answer = 1
    for key in clothes:
      answer *= (clothes[key] + 1)

    print(answer - 1)
