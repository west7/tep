def main():
    n = int(input())
    sin = list(map(int, input().split()))
    k = n
    for _ in range(n):
        for i in range(k - 1):
            sin[i] = 1 if sin[i] == sin[i + 1] else -1
        k -= 1
    print('branca' if sin[0] == -1 else 'preta')

if __name__ == '__main__':
    main()
