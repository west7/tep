def main():
    ns = [int(input()) for _ in range(5)]  
    fst = [0, 0]
    snd = [0, 0]
    for n in ns:
        if n > fst[0]:
            fst[0] = n
            fst[1] = 1
            continue
        if n > snd[0] and n != fst[0]:
            snd[0] = n
            snd[1] = 1
            continue
        if  n == fst[0]:
            fst[1] += 1
            continue
        if n == snd[0]:
            snd[1] += 1

    print(f'{fst[1]} {snd[1]}')

if __name__ == '__main__':
    main()
