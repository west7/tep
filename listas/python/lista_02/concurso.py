def main():
    _, k = map(int, input().split())
    as_ = list(map(int, input().split()))
    as_.sort(reverse=True)
    print(as_[k-1])


if __name__ == '__main__':
    main()