def main():
    print('Введите массив числе через пробел')
    a = input().split() or [1, 2, 3, 4]
    a = list(map(lambda x: int(x), a))
    print(a)
    print('Введите массив числе через пробел')
    b = input().split() or [3, 4, 5, 6]
    b = list(map(lambda x: int(x), b))
    print(b)
    print(diff_lists(a, b))

def diff_lists(a, b):
    result = set(b) - set(a)
    return list(result)

if __name__ == "__main__":
    main()