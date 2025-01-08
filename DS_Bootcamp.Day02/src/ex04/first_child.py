import sys
from random import randint


def check_file(result: list):
    if len(result[0].strip().split(',')) > 2:
        raise ValueError("Many values")

    for line in result[1:]:
        line_split = line.strip().split(',')
        if len(line_split) > 2:
            raise ValueError("Many values")
        try:
            a, b = int(line_split[0]), int(line_split[1])
        except ValueError:
            raise ValueError("Not digit")
        if not ((a == 0 or a == 1) and (b == 0 or b == 1)):
            raise ValueError("Values != 0/1")
        if a == b:
            raise ValueError("Double value")

    return True

def to_list(data: list, header: bool):
    flag = 1 if header else 0
    return [list(map(int, line.strip().split(","))) for line in data[flag:]]


class Research:
    def __init__(self, path):
        self.path = path
        self.my_list = self.file_reader()
        self.calc = self.Calculations(self.my_list)
        self.analytics = self.Analytics(self.my_list)

    def file_reader(self, has_header=True):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
                if check_file(lines):
                    my_list = to_list(lines, has_header)
                    return my_list
        except (FileNotFoundError, FileExistsError) as error:
            print(f"Error: {error}")

    class Calculations:
        def __init__(self, data_list):
            self.data_list = data_list

        def counts(self):
            count_zero = sum(1 for a, b in self.data_list if int(a) == 0)
            count_one = sum(1 for a, b in self.data_list if int(a) == 1)
            return count_one, count_zero

        def fractions(self, zero_count: int, one_count: int):
            sum_count = zero_count + one_count
            zero_p =  zero_count / sum_count * 100
            one_p = one_count / sum_count * 100
            return zero_p, one_p

    class Analytics(Calculations):
        def predict_random(self, count_random: int):
            random_list = [[0, 1], [1, 0]]
            result = []
            for i in range(count_random):
                result.append(random_list[randint(0, 1)])
            return result

        def predict_last(self):
            return self.data_list[-1]

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            research = Research(filename)
            for_print = research.file_reader()
            if for_print is not None:
                print(for_print)
                zero, one = research.calc.counts()
                print(zero, one)
                zero_percent, one_percent = research.calc.fractions(zero, one)
                print(zero_percent, one_percent)
                print(research.analytics.predict_random(3))
                print(research.analytics.predict_last())
    except ValueError as e:
        print(f'Error: {e}')


