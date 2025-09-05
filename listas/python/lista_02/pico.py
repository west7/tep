def main():
    n = int(input())
    ns = list(map(int, input().split()))
    for i in range(1, n-1):
        if ns[i-1] > ns[i] and ns[i] < ns[i+1]:
            print('S')
            return
    print('N')


if __name__ == '__main__':
    main()
