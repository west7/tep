def main():
    n = int(input())
    fita = list(map(int, input().split()))
    last_zero = fita.index(0)
    for i in range(n):
        if fita[i] == 0:
            last_zero = i
            continue
        color = min(abs(i - last_zero), 9)
        fita[i] = color

    for i in range(n - 1, -1, -1):
        if fita[i] == 0:
            last_zero = i
            continue
        color = min(abs(i - last_zero), 9)
        if fita[i] > color:
            fita[i] = color

    print(*fita)

if __name__ == '__main__':
    main()
