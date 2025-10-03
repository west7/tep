#!/usr/bin/python3
def main():
    Q = int(input())
    qs = [list(map(int, input().split())) for _ in range(Q)]
    s = dict()
    min_key = float("inf")
    max_key = float("-inf")
    for q in qs:
        action = q[0]
        match action:
            case 1:
                key = q[1]
                s[key] = s.get(key, 0) + 1
                min_key = min(min_key, key)
                max_key = max(max_key, key)
            case 2:
                key = q[1]
                c = q[2]
                less = min(c, s.get(key, c + 1))
                s[key] = s.get(key, 0) - less
                if s[key] == 0:
                    del s[key]
                    if key == min_key or key == max_key:
                        if s:
                            min_key = min(s.keys())
                            max_key = max(s.keys())
                        else:
                            min_key = float("inf")
                            max_key = float("-inf")
            case 3:
                print(max_key - min_key)


if __name__ == "__main__":
    main()
