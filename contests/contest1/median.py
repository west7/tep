#!/usr/bin/python3

def main():
    a, b, c = map(int, input().split())
    ns = [a, b, c]
    ns.sort()
    if ns[1] == b:
        print('Yes')
    else:
        print('No')
    

if __name__ == '__main__':
    main()