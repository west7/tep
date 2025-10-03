#!/usr/bin/python3
def main():
    N, A, B = map(int, input().split())
    total = N * (N + 1) // 2
    c_A = N // A
    tot_A = A * c_A * (c_A + 1) // 2
    c_B = N // B
    tot_B = B * c_B * (c_B + 1) // 2
    a, b = A, B
    while b:
        a, b = b, a % b
    lcm = A * B // a
    c_AB = N // lcm
    tot_AB = lcm * c_AB * (c_AB + 1) // 2
    print(total - (tot_A + tot_B - tot_AB))

if __name__ == "__main__":
    main()
