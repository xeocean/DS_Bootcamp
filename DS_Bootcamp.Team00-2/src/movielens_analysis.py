import re
import requests
from datetime import datetime
from collections import Counter, defaultdict
from functools import lru_cache
from bs4 import BeautifulSoup


'''----------------------------------------------------------------'''
def calculate_mean(data):
    """
    Вычисляет среднее значение списка чисел.
    """
    return sum(data) / len(data) if data else 0

def calculate_median(data):
    """
    Вычисляет медиану списка чисел.
    """
    if not data:
        return 0

    sorted_data = sorted(data)
    mid = len(sorted_data) // 2

    return (sorted_data[mid - 1] + sorted_data[mid]) / 2 if len(sorted_data) % 2 == 0 else sorted_data[mid]

def calculate_variance(data):
    """
    Вычисляет дисперсию списка чисел.
    """
    if len(data) < 2:
        return 0

    mean_value = calculate_mean(data)
    
    return sum((x - mean_value) ** 2 for x in data) / (len(data) - 1)

class Ratings:
    """
    Анализ данных из файла ratings.csv
    """
    def __init__(self, path_to_the_file):
        self.path = path_to_the_file
        self.data = []
        self.load_data()

    def load_data(self):
        """
        Загружает данные из CSV-файла в список словарей.
        """
        try:
            with open(self.path, 'r') as file:
                header = file.readline().strip().split(',')
                for line in file:
                    row = line.strip().split(',')
                    self.data.append({
                        "userId": int(row[0]),
                        "movieId": int(row[1]),
                        "rating": float(row[2]),
                        "timestamp": int(row[3])
                    })
        except FileNotFoundError:
            print(f"Файл {self.path} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    class Movies:
        def __init__(self, ratings_data):
            self.ratings_data = ratings_data

        @lru_cache
        def dist_by_year(self):
            """
            Возвращает словарь, где ключи — годы, а значения — количество рейтингов.
            Отсортирован по возрастанию годов.
            """
            ratings_by_year = Counter(
                datetime.fromtimestamp(entry["timestamp"]).year for entry in self.ratings_data
            )
            return dict(sorted(ratings_by_year.items()))

        @lru_cache
        def dist_by_rating(self):
            """
            Возвращает словарь, где ключи — рейтинги, а значения — количество.
            Отсортирован по возрастанию рейтингов.
            """
            ratings_distribution = Counter(entry["rating"] for entry in self.ratings_data)
            return dict(sorted(ratings_distribution.items()))

        @lru_cache
        def top_by_num_of_ratings(self, n):
            """
            Возвращает топ-n фильмов по количеству рейтингов.
            Ключи — movieId, значения — количество.
            Отсортирован по убыванию количества.
            """
            movie_counts = Counter(entry["movieId"] for entry in self.ratings_data)
            return dict(movie_counts.most_common(n))

        @lru_cache
        def top_by_ratings(self, n, metric=calculate_mean):
            """
            Возвращает топ-n фильмов по средней или медианной оценке.
            Ключи — movieId, значения — значение метрики.
            Отсортирован по убыванию метрики.
            """
            movie_ratings = defaultdict(list)
            for entry in self.ratings_data:
                movie_ratings[entry["movieId"]].append(entry["rating"])

            metrics = {
                movie: round(metric(ratings), 2)
                for movie, ratings in movie_ratings.items()
            }
            
            return dict(sorted(metrics.items(), key=lambda x: x[1], reverse=True)[:n])

        @lru_cache
        def top_controversial(self, n):
            """
            Возвращает топ-n фильмов по дисперсии оценок.
            Ключи — movieId, значения — дисперсия.
            Отсортирован по убыванию дисперсии.
            """
            movie_ratings = defaultdict(list)
            
            for entry in self.ratings_data:
                movie_ratings[entry["movieId"]].append(entry["rating"])

            variances = {
                movie: round(calculate_variance(ratings), 2)
                for movie, ratings in movie_ratings.items()
                if len(ratings) > 1
            }
            
            return dict(sorted(variances.items(), key=lambda x: x[1], reverse=True)[:n])

    class Users(Movies):
        def __init__(self, ratings_data):
            super().__init__(ratings_data)

        @lru_cache
        def dist_by_num_of_ratings(self):
            """
            Возвращает словарь, где ключи — userId, а значения — количество рейтингов.
            Отсортирован по возрастанию userId.
            """
            user_ratings = Counter(entry["userId"] for entry in self.ratings_data)
            return dict(sorted(user_ratings.items()))

        @lru_cache
        def dist_by_average_rating(self, metric=calculate_mean):
            """
            Возвращает словарь, где ключи — userId, а значения — средние или медианные оценки.
            Отсортирован по возрастанию userId.
            """
            user_ratings = defaultdict(list)
            
            for entry in self.ratings_data:
                user_ratings[entry["userId"]].append(entry["rating"])

            metrics = {
                user: round(metric(ratings), 2)
                for user, ratings in user_ratings.items()
            }
            
            return dict(sorted(metrics.items()))

        @lru_cache
        def top_by_variance(self, n):
            """
            Возвращает топ-n пользователей по дисперсии их оценок.
            Ключи — userId, значения — дисперсия.
            Отсортирован по убыванию дисперсии.
            """
            user_ratings = defaultdict(list)
            
            for entry in self.ratings_data:
                user_ratings[entry["userId"]].append(entry["rating"])

            variances = {
                user: round(calculate_variance(ratings), 2)
                for user, ratings in user_ratings.items()
                if len(ratings) > 1
            }
            
            return dict(sorted(variances.items(), key=lambda x: x[1], reverse=True)[:n])


'''----------------------------------------------------------------'''

# Модуль links

class Links:

    def __init__(self, path_to_the_file, count_load=None):

        self.path_to_the_file = path_to_the_file
        self.data = list(self.load_data(count_load))

    def load_data(self, n=None):
        with open(self.path_to_the_file, 'r') as file:
            for number_line, line in enumerate(file):
                if number_line == 0:
                    continue
                elif n and number_line > n:
                    break
                else:
                    yield line

    def replace_id(self, list_movie_id: list):
        list_current_imdb = []
        list_movie_id = list(map(str, list_movie_id))
        for line in self.data:
            for search_id_imdb in list_movie_id:
                movie_id = line.split(",")[0].strip()
                imdb_id = line.split(",")[1].strip()
                if movie_id == search_id_imdb:
                    list_current_imdb.append(imdb_id)

        return list_current_imdb

    def get_imdb(self, list_of_movies: list, list_of_fields: list):

        imdb_list = self.replace_id(list_of_movies)
        imdb_info = []
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

        for key_movie in imdb_list:

            try:
                url = f"http://www.imdb.com/title/tt{key_movie}/"
                response = requests.get(url, headers=headers)
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                continue

            if response.status_code == 200:
                movie_info = [key_movie]
                soup = BeautifulSoup(response.content, "html.parser")

                if 'title' in (field_all.lower() for field_all in list_of_fields):
                    movie_info.append(soup.find("h1").text)

                for find_value in list_of_fields:
                    if find_value.lower() != 'title':
                        found = False
                        blocks_for_search = soup.find_all("li", role="presentation")
                        for block in blocks_for_search:
                            if find_value.lower() in block.text.lower():
                                found = True
                                value = block.find("div") or block.find("a") or block.find("span")
                                if value:
                                    # print(find_value, value.text.strip()) # Debug info
                                    movie_info.append(value.text.strip())
                                break

                        if not found:
                            movie_info.append(None)
                            # print(find_value, None) # Debug info

                imdb_info.append(movie_info)

        imdb_info = sorted(imdb_info, key=lambda x: x[0] if x and x[0] else "", reverse=True)

        return imdb_info

    def top_directors(self, n):

        directors = {}
        list_movies = [i for i in range(len(self.data) + 1)]
        parse = self.get_imdb(list_movies, ["Director"])
        for item in parse:
            director = item[1]
            if director not in directors:
                directors[director] = 1
            else:
                directors[director] += 1

        directors = sorted(directors.items(), key=lambda x: x[1], reverse=True)

        return dict(directors[:n])

    def most_expensive(self, n):

        budgets = {}
        list_movies = [i for i in range(len(self.data))]
        parse = self.get_imdb(list_movies, ["Title", "Budget"])
        for item in parse:
            title = item[1]
            budget = item[2]
            if title not in budgets:
                budgets[title] = budget

        budgets = sorted(budgets.items(), key=lambda x: x[1] if x[1] is not None else "", reverse=True)

        return dict(budgets[:n])

    def most_profitable(self, n):

        profitable = {}
        list_movies = [i for i in range(len(self.data))]
        parse = self.get_imdb(list_movies, ["Title", "Budget", "Gross worldwide"])
        for item in parse:
            title = item[1]
            budget = item[2] if item[2] else '0'
            gross = item[3] if item[3] else '0'
            budget = int(re.sub(r"[^\d]", "", budget))
            gross = int(re.sub(r"[^\d]", "", gross))
            # print(budget, gross)
            if title not in profitable:
                profitable[title] = gross - budget

        profitable = sorted(profitable.items(), key=lambda x: x[1] if x[1] is not None else "", reverse=True)

        return dict(profitable[:n])

    def longest(self, n):

        runtimes = {}
        list_movies = [i for i in range(len(self.data))]
        parse = self.get_imdb(list_movies, ["Title", "Runtime"])
        for item in parse:
            title = item[1]
            hours_match = re.search(r"(\d+)\s*hour", item[2])
            minutes_match = re.search(r"(\d+)\s*minute", item[2])
            hours = int(hours_match.group(1)) if hours_match else 0
            minutes = int(minutes_match.group(1)) if minutes_match else 0
            runtime = hours * 60 + minutes
            if title not in runtimes:
                runtimes[title] = runtime

        runtimes = sorted(runtimes.items(), key=lambda x: x[1] if x[1] is not None else "", reverse=True)

        return dict(runtimes[:n])

    def top_cost_per_minute(self, n):

        costs = {}
        list_movies = [i for i in range(len(self.data))]
        parse = self.get_imdb(list_movies, ["Title", "Budget", "Runtime"])
        for item in parse:
            title = item[1]
            budget = item[2] if item[2] else '0'
            budget = int(re.sub(r"[^\d]", "", budget))
            hours_match = re.search(r"(\d+)\s*hour", item[3])
            minutes_match = re.search(r"(\d+)\s*minute", item[3])
            hours = int(hours_match.group(1)) if hours_match else 0
            minutes = int(minutes_match.group(1)) if minutes_match else 0
            runtime = hours * 60 + minutes
            cost = budget / runtime
            if title not in costs:
                costs[title] = round(cost, 2)

        costs = sorted(costs.items(), key=lambda x: x[1] if x[1] is not None else "", reverse=True)

        return dict(costs[:n])

    def top_languages(self, n):

        languages = {}
        list_movies = [i for i in range(len(self.data))]
        parse = self.get_imdb(list_movies, ["Languages"])
        for item in parse:
            language_match = re.split(r'(?=[A-Z])', item[1]) if item[1] is not None else ""
            temp_list = [language for language in language_match if language]
            for value in temp_list:
                if value not in languages:
                    languages[value] = 1
                else:
                    languages[value] += 1

        languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

        return dict(languages[:n])

class Movies:
    """
    Анализ данных из movies.py
    """

    def __init__(self, file_path: str):
        self.path: str = file_path
        self.data = self.__get_data()

    def __get_data(self):
        """
        Загружает данные из CSV-файла в список строк.
        """
        try:
            with open(self.path, "r") as file:
                for line in file:
                    yield line
        except FileNotFoundError:
            print(f"Файл {self.path} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def dist_by_release(self):
        """
        Возращает словарь c ключом - год, значение - кол-во релизов в год.
        Список отсортирован в убывающем порядке по вхождениям.
        """
        years = []

        for line in self.data:

            line = line.strip("\n")

            if line == "" or line == "movieId,title,genres":  # первая и последняя строчка
                continue

            try:
                match = re.match(r'(\d+),((".*?"|[^,]+)),(.+)', line)

                year = re.search(r"((\d{4}))", match.group(2).strip('"'))

                if year == None:  # There are no year in the film title (че за броук дату собирал йоу)
                    continue

                years.append(int(year.group(1)))
            except Exception as e:
                print(f"Ошибочка: {e}.")

        return dict(sorted(Counter(years).items(), key=lambda item: item[1], reverse=True))

    def dist_by_genres(self):
        """
        Возращает словарь c ключом - жанр, значение - кол-во жанров во всех фильмах.
        Словарь отсортирован в убывающем порядке по вхождениям.
        """
        genres = []

        for line in self.data:

            line = line.strip("\n")

            if line == "" or line == "movieId,title,genres":  # первая и последняя строчка
                continue

            try:
                match = re.match(r'(\d+),((".*?"|[^,]+)),(.+)', line)

                genres += match.group(4).split("|")

            except Exception as e:
                print(f"Ошибочка: {e}.")

        return dict(sorted(Counter(genres).items(), key=lambda item: item[1], reverse=True))

    def most_genres(self, n: int):
        """
        Возвращает словарь с топ-н фильмами, где ключи - названия фильмов,
        а значения - количество жанров для каждого фильма.
        Отсортировано по количеству жанров в порядке убывания.
        """
        movies_with_genres_count = {}

        for line in self.data:
            line = line.strip("\n")

            if line == "" or line == "movieId,title,genres":
                continue

            try:
                match = re.match(r'(\d+),((".*?"|[^,]+)),(.+)', line)

                title = match.group(2).strip('"')

                genres = match.group(4).split("|")
                movies_with_genres_count[title] = len(genres)
            except Exception as e:
                print(line)
                print(f"Ошибочка: {e}")

        return dict(sorted(movies_with_genres_count.items(), key=lambda x: x[1], reverse=True)[:n])


# Tags


class Tags:
    """
    Анализ данных из файла tags.csv
    """

    def __init__(self, file_path: str):
        self.path: str = file_path

    def __get_data(self):
        """
        Загружает данные из CSV-файла в список строк.
        """
        try:
            with open(self.path, "r") as file:
                next(file)
                for line in file:
                    yield line.split(",")
        except FileNotFoundError:
            print(f"Файл {self.path} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def most_words(self, n: int):
        """
        Возвращает top-n тегов с наибольшим количеством слов.
        Это словарь, где ключи - теги, а значения - количество слов в каждом теге.
        """
        self.data = self.__get_data()
        big_tags = {}

        try:
            for _, _, tag, _ in self.data:
                big_tags[tag] = len(tag.split(" "))
        except Exception as e:
            print(f"Oshipka: {e}")

        return dict(sorted(big_tags.items(), key=lambda x: x[1], reverse=True)[:n])

    def longest(self, n: int):
        """
        Возвращает список top-n самых длинных тегов по количеству символов.
        """
        self.data = self.__get_data()
        big_tags = {}

        try:
            for _, _, tag, _ in self.data:
                big_tags[tag] = len(tag)
        except Exception as e:
            print(f"Oshipka: {e}")

        return [x[0] for x in sorted(big_tags.items(), key=lambda x: x[1], reverse=True)[:n]]

    def most_words_and_longest(self, n: int):
        """
        Возвращает список пересечения между top-n тегами с наибольшим количеством слов
        и top-n самыми длинными тегами по количеству символов.
        """

        most_chars = set(self.longest(n))
        most_words = set(self.most_words(n).keys())

        return list(most_words.intersection(most_chars))

    def most_popular(self, n: int):
        """
        The method returns the most popular tags.
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        self.data = self.__get_data()
        most_popular = {}
        try:
            most_popular = sorted(
                Counter([tag for _, _, tag, _ in self.data]).items(),
                key=lambda x: x[1],
                reverse=True,
            )[:n]
        except Exception as e:
            print(f"Oshipka: {e}.")
        return dict(most_popular)

    def tags_with(self, word: str):
        """
        Возвращает список всех уникальные теги, которые содержат данное слово.
        Сортирует по названиям тегов в алфавитном порядке.
        """
        tags_with_word = set()
        self.data = self.__get_data()

        try:

            tags_with_word = set([tag for _, _, tag, _ in self.data if word in tag.split(" ")])
        except Exception as e:
            print(f"Oshipka: {e}.")

        return sorted(tags_with_word)
