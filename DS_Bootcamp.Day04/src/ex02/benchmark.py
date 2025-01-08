import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
          'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']


def list_loop():
    my_list = []
    for email in emails:
        if email.endswith("gmail.com"):
            my_list.append(email)


def list_comprehension():
    my_list = [email for email in emails if email.endswith("gmail.com")]


def list_map():
    my_list = list(map(lambda email: email if email.endswith("gmail.com") else None, emails))


def list_filter():
    my_list = list(filter(lambda email: email.endswith("gmail.com"), emails))


if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            names = ['loop', 'list comprehension', 'map', 'filter']
            name, count, time = sys.argv[1], int(sys.argv[2]), 0
            if count > 0 and name in names:
                match name:
                    case 'loop':
                        time = timeit.timeit(list_loop, number=count)
                    case 'list comprehension':
                        time = timeit.timeit(list_comprehension, number=count)
                    case 'map':
                        time = timeit.timeit(list_map, number=count)
                    case 'filter':
                        time = timeit.timeit(list_filter, number=count)
                print(time)
    except ValueError as e:
        print(f'{e}')
