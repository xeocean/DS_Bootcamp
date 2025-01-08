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


if __name__ == "__main__":
    time1 = timeit.timeit(list_loop, number=90000000)
    time2 = timeit.timeit(list_comprehension, number=90000000)
    time_sorted = sorted([time1, time2])
    if time1 < time2: print('it is better to use a list loop')
    else: print('it is better to use a list comprehension')
    print(f'{time_sorted[0]} vs {time_sorted[1]}')

