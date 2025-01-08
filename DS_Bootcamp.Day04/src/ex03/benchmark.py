import timeit
import sys
from functools import reduce


def sum_loop(n):
    result = 0
    for i in range(n + 1):
        result += i * i
    return result


def sun_reduce(n):
    result = reduce(lambda total, i: total + i * i, range(n + 1))
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            names = ['loop', 'reduce']
            name, count, number, time = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), 0
            if count > 0 and number > 0 and name in names:
                match name:
                    case 'loop':
                        time = timeit.timeit(lambda: sum_loop(number), number=count)
                    case 'reduce':
                        time = timeit.timeit(lambda: sun_reduce(number), number=count)
                print(time)
    except ValueError as e:
        print(f'{e}')
