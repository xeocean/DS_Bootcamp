from random import randint
import logging
import requests
from config import TOKEN, CHAT_ID

logging.basicConfig(level=logging.INFO, filename="analytics.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

def check_file(result: list):
    if len(result[0].strip().split(',')) > 2:
        logging.error("Many values")
        raise ValueError("Many values")

    for line in result[1:]:
        line_split = line.strip().split(',')
        if len(line_split) > 2:
            logging.error("Many values")
            raise ValueError("Many values")
        try:
            a, b = int(line_split[0]), int(line_split[1])
        except ValueError:
            logging.error("Not digit")
            raise ValueError("Not digit")
        if not ((a == 0 or a == 1) and (b == 0 or b == 1)):
            logging.error("Values not equal to 0 or 1")
            raise ValueError("Values not equal to 0 or 1")
        if a == b:
            logging.error("Duplicate values")
            raise ValueError("Duplicate values")

    return True

def to_list(data: list, header: bool):
    flag = 1 if header else 0
    return [list(map(int, line.strip().split(","))) for line in data[flag:]]


class Research:
    def __init__(self):
        self.path = None
        self.my_list = None
        self.calc = None
        self.analytics = None

    def set_attributes(self, path):
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
                    logging.info("File is read")
                    return my_list
        except (FileNotFoundError, FileExistsError) as error:
            logging.error("File is not read")

    def save_file(self, text, filename, extension="txt"):
        try:
            with open(f'{filename}.{extension}', 'w') as file:
                file.write(text)
                logging.info("File is save")
        except (FileNotFoundError, FileExistsError) as error:
            logging.error("File is not save")

    def send_message(self, status: bool):
        if status:
            payload = {"chat_id": CHAT_ID, "text": "The report has been successfully created"}
        else:
            payload = {"chat_id": CHAT_ID, "text": "The report hasn’t been created due to an error"}
        response = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
        if response.status_code == 200:
            logging.info("Send message")
        else:
            logging.error("Don`t send message, status code: %d", response.status_code)

    class Calculations:
        def __init__(self, data_list):
            self.data_list = data_list

        def counts(self, data_list: list):
            count_zero = sum(1 for a, b in data_list if int(a) == 0)
            count_one = sum(1 for a, b in data_list if int(a) == 1)
            logging.info("Calculation counts")
            return count_one, count_zero

        def fractions(self, zero_count: int, one_count: int):
            sum_count = zero_count + one_count
            zero_p =  zero_count / sum_count * 100
            one_p = one_count / sum_count * 100
            logging.info("Calculation fractions")
            return zero_p, one_p

    class Analytics(Calculations):
        def predict_random(self, count_random: int):
            random_list = [[0, 1], [1, 0]]
            result = []
            for i in range(count_random):
                result.append(random_list[randint(0, 1)])
            logging.info("Analytics %d predict", count_random)
            return result

        def predict_last(self):
            logging.info("Return last")
            return self.data_list[-1]

