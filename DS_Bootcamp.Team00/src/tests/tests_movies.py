import pytest
from unittest.mock import mock_open, patch
from movielens_analysis import Movies

@pytest.fixture
def mock_movie_data():
    return (
        "movieId,title,genres\n"
        "1,The Shawshank Redemption (1994),Drama|Crime\n"
        "2,The Godfather (1972),Drama|Crime\n"
        "3,The Dark Knight (2008),Action|Crime|Drama\n"
        "4,Pulp Fiction (1994),Crime|Drama\n"
        "5,Forrest Gump (1994),Drama|Romance\n"
        "6,Inception (2010),Sci-Fi|Action\n"
        "7,The Matrix (1999),Sci-Fi|Action\n"
    )

@pytest.fixture
def movies(mock_movie_data):
    with patch("builtins.open", mock_open(read_data=mock_movie_data)):
        yield Movies("movies.csv")

class TestMovies:

    def test_get_data(self, movies):
        data = list(movies._Movies__get_data())
        assert len(data) == 8

    def test_dist_by_release(self, movies):
        expected_result = {1994: 3, 1972: 1, 2008: 1, 2010: 1, 1999: 1}
        result = movies.dist_by_release()
        assert expected_result == result

    def test_dist_by_genres(self, movies):
        expected_result = {"Drama": 5, "Crime": 4, "Action": 3, "Romance": 1, "Sci-Fi": 2}
        result = movies.dist_by_genres()
        assert expected_result == result

    def test_most_genres(self, movies):
        result = movies.most_genres(3)
        assert "The Dark Knight (2008)" in result
        assert result["The Dark Knight (2008)"] == 3