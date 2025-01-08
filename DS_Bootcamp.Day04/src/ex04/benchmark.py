import timeit
import random
from collections import Counter


def my_function(values):
    my_dict = {}
    for value in values:
        if value not in my_dict:
            my_dict[value] = 1
        else:
            my_dict[value] += 1
    return my_dict


def my_top(values):
    my_dict = {}
    for value in values:
        if value not in my_dict:
            my_dict[value] = 1
        else:
            my_dict[value] += 1
    sort = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    return sort[:10]


def my_counter(values):
    return dict(Counter(values))


def my_counter_top(values):
    return Counter(values).most_common(10)


if __name__ == "__main__":
    my_iter = [random.randint(0, 100) for i in range(1000000)]
    time1 = timeit.timeit(lambda: my_function(my_iter), number=10)
    time2 = timeit.timeit(lambda: my_counter(my_iter), number=10)
    time3 = timeit.timeit(lambda: my_top(my_iter), number=10)
    time4 = timeit.timeit(lambda: my_counter_top(my_iter), number=10)
    print(f'my function: {time1}')
    print(f'Counter: {time2}')
    print(f'my top: {time3}')
    print(f'Counter\'s top: {time4}')
