def solve(n: int, cs: list) -> bool:
    if cs[0] > 8:
        return False
    for i in range(n - 1):
        if cs[i+1] - cs[i] > 8:
            return False
    return True

def main():
    n = int(input())
    cs = sorted(list(map(int, input().split())))
    print('S' if solve(n, cs) else 'N')

    
if __name__ == '__main__':
    main()
