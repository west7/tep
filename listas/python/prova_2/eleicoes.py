def main():
    A, B, N = map(int, input().split())
    r = int((N // A) * B)
    print(r)

if __name__ == "__main__":
    main()