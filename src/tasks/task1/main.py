from functools import reduce
import re

def main():
    print('Input string')
    value = input()
    pattern = r'^\S+\.txt$'
    content = ''
    if (re.match(pattern, value)):
        content = read_file(value)
    else:
        content = value
        
    result = count_words(content)

    print(result)

def count_words(value):
    words = value.split()
    return reduce(
        lambda acc, word: {**acc, word.lower(): acc.get(word.lower(), 0) + 1},
        words,
        {}
    )

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')
        return ''


if __name__ == "__main__":
    main()