import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:

        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')

    if len(sys.argv) > 2:
        num_start = sys.argv[1]
        num_end = sys.argv[2]
        with open('bakery.csv', 'r') as f:
            for i, line in enumerate(f):
                if int(num_start) - 1 <= i <= int(num_end) - 1:
                    print(line, end='')

    else:
        num_start = sys.argv[1]
        with open('bakery.csv', 'r') as f:
            for i, line in enumerate(f):
                if i >= int(num_start) - 1:
                    print(line, end='')


