def main():
    _ = int(input())
    st = input()
    stack = []
    for s in st:
        if stack and s != stack[-1]:
            stack.pop()
            continue
        stack.append(s)

    print(len(stack))

        
if __name__ == '__main__':
    main()
