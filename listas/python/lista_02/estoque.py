def main():
    n = int(input())
    ns = [int(input()) for _ in range(n)]
    p = int(input())
    count = 0
    for _ in range(p):
        sz = int(input())
        sz -= 1
        if ns[sz] == 0:
            continue
        ns[sz] -= 1
        count += 1
    print(count)  




if __name__ == '__main__':
    main()