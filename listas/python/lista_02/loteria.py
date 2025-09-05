def main():
    xs = list(map(int, input().split()))
    ns = list(map(int, input().split()))
    count = 0
    for x in xs:
        if x in ns:
            count +=1
            
    match count:
        case 3:
            print('terno')
        case 4:
            print('quadra')
        case 5:
            print('quina')
        case 6:
            print('sena')
        case _:
            print('azar')

if __name__ == '__main__':
    main()
