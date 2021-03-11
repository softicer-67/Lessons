import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:

        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for i in f:
                i = str(i)
                print(f'{i}', end='')

    elif len(sys.argv) > 2:
        num_start = sys.argv[1]
        num_end = sys.argv[2]
        with open('bakery.csv', 'r') as f:
            num = f.readlines()
            for i in range(int(num_start) - 1, int(num_end)):
                print(num[i], end='')

    else:
        num_start = sys.argv[1]
        with open('bakery.csv', 'r') as f:
            num = f.readlines()
            for i in range(int(num_start) - 1, len(num)):
                print(num[i], end='')
