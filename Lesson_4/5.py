from utils import currency_rates
import sys


if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit(1)
currency_rates(sys.argv[1])
