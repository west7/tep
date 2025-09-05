def main():
    n   = int(input())
    ns  = [int(input()) for _ in range(n)]
    pos = [0] * (n + 1)

    for i, atlt in enumerate(ns):
        pos[atlt] = i
    
    for i in range(1, n + 1):
        print(pos[i] + 1)

if __name__ == '__main__':
    main()  

