import timeit

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


if __name__ == "__main__":
    time1 = timeit.timeit(list_loop, number=90000000)
    time2 = timeit.timeit(list_comprehension, number=90000000)
    time3 = timeit.timeit(list_map, number=90000000)
    time_sorted = sorted([(time1, "list loop"), (time2, "list comprehension"), (time3, "map")])
    print(f'it is better to use a {time_sorted[0][1]}')
    print(f'{time_sorted[0][0]} vs {time_sorted[1][0]} vs {time_sorted[2][0]}')