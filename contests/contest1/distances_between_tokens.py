#!/usr/bin/python3

def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        row = input()
        grid.append(row)
    distance = 0
    first = False
    x0, y0 = -1, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'o':
                if first:
                    distance = abs(i - x0) + abs(j - y0)
                first = True
                x0 = i
                y0 = j
    print(distance)

    

if __name__ == '__main__':
    main()