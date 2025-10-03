def main():
    st = list(input())
    stack = []
    longest = 0
    num = 0
    l = 0
    for i in range(len(st)):
        s = st[i]
        if s == '(':
            stack.append(s)
        elif s == ')' and stack:
            stack.pop()
            l += 2
            if not stack or i == len(st) - 1 or (st[i+1] == '(' and i + 1 == len(st) - 1):
                if l > longest:
                    longest = l
                num += 1
                l = 0

    print(longest, 1 if num == 0 else num)


if __name__ == '__main__':
    main()