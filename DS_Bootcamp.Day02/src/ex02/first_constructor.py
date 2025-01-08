import sys


def check_file(result):
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


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
                if check_file(lines):
                    return "".join(lines)
        except (FileNotFoundError, FileExistsError) as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            research = Research(filename)
            for_print = research.file_reader()
            if for_print is not None:
                print(for_print)
    except ValueError as e:
        print(f'Error: {e}')
