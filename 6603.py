import sys; input = sys.stdin.readline;
from itertools import combinations
if __name__ == '__main__':

    while True:

        arr = list(map(int, input().split())) # 테스트 케이스 입력 받기

        # 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.
        k = arr[0]
        s = arr[1:]

        # 입력의 마지막 줄에는 0이 하나 주어진다.
        if k == 0:
            break

        # 조합(combination) 사용
        #   조합: 순서를 고려하지 않고 중복 없이 뽑을 때 경우의 수
        for comb in combinations(s, 6):
            temp = list(map(str, comb))
            print(" ".join(temp))
        print()
