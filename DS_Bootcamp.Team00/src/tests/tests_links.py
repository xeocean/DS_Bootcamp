from movielens_analysis import Links

class TestLinks:
    test_links = Links("ml-latest-small/links.csv", 5)

    def test_get_imdb(self):
        list_movies = [1, 2, 3]
        list_fields = ['Director', 'Budget', 'Gross worldwide', 'Runtime', 'Language', 'None']
        result = self.test_links.get_imdb(list_movies, list_fields)
        assert type(result) == list
        for one in result:
            assert type(one) == list
            assert len(one) == len(list_fields) + 1

    def test_get_imdb_pass_incorrect(self):
        list_movies = [1, 0, 3]
        list_fields = ['Director', 'Budget', 'Gross worldwide', 'Runtime', 'Language', 'None']
        result = self.test_links.get_imdb(list_movies, list_fields)
        assert type(result) == list
        assert len(result) == 2
        for one in result:
            assert type(one) == list
            assert len(one) == len(list_fields) + 1

    def test_top_director(self):
        result = self.test_links.top_directors(5)
        assert type(result) == dict

    def test_top_budget(self):
        result = self.test_links.most_expensive(5)
        assert type(result) == dict

    def test_top_profitable(self):
        result = self.test_links.most_profitable(5)
        assert type(result) == dict

    def test_top_runtime(self):
        result = self.test_links.longest(5)
        assert type(result) == dict

    def test_top_cost(self):
        result = self.test_links.top_cost_per_minute(5)
        assert type(result) == dict

    def test_top_languages(self):
        result = self.test_links.top_languages(5)
        assert type(result) == dict
