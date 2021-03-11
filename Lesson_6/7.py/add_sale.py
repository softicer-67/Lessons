import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit(1)
    save = sys.argv[1]

    lines = 1
    with open('bakery.csv', mode='r+', encoding='utf-8') as file:
        for line in file:
            lines += 1
        file.write(f'{lines}: {save}\n')
