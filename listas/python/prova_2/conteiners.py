def main():
    n = int(input())
    tot = sum(int(input()) for _ in range(n))
    print(f'Carga total: {tot} kilogramas')

if __name__ == '__main__':
    main()