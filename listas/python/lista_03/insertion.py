def main():
    n = int(input())
    st = list(input())
    stack = []
    pair = {
        '(' : None,
        ')' : '('
    }
    for s in st:
        if stack and pair[s] == stack[-1]:
            stack.pop()
            continue
        stack.append(s)

    for bracket in stack:
        if bracket == ')':
            st.insert(0, '(')
        elif bracket == '(':
            st.append(')')

    print(''.join(st))

if __name__ == '__main__':
    main()