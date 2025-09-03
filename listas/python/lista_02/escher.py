def is_escher(size: int, ns: list) -> bool:
    """ if len(ns) % 2 != 0:
        return False """
    s = ns[0] + ns[-1]
    for i in range(1, size + 1):
        s_ = ns[i] + ns[-(i+1)]
        if s != s_:
            return False
    return True


def main():
    n = int(input())
    ns = list(map(int, input().split()))
    size = n // 2
    print('S' if is_escher(size, ns) else 'N')

if __name__ == '__main__':
    main()
