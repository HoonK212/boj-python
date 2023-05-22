import sys; input = sys.stdin.readline; sys.setrecursionlimit(10 ** 6)
if __name__ == '__main__':

    def draw_star(size):

        # 더 이상 나눌 수 없는 최소 단위를 찾아, '*' return
        if size == 1:
            return ['*']
        stars = draw_star(size // 3)
        line = []

        # 13, 17 line의 append와는 다르게
        #   16 line의 append에서는 size//3만큼의 blank가 필요하다는 것이 핵심 !!!
        for s in stars:
            line.append(s * 3)
        for s in stars:
            line.append(s + ' ' * (size // 3) + s)
        for s in stars:
            line.append(s * 3)
        return line


    n = int(input())
    print('\n'.join(draw_star(n)))
