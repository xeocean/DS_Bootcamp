import tempfile
import pytest
from movielens_analysis import Ratings, calculate_mean, calculate_median


@pytest.fixture
def sample_ratings():
    data = [
        {"userId": 1, "movieId": 101, "rating": 3.5, "timestamp": 1000000000},
        {"userId": 1, "movieId": 102, "rating": 4.0, "timestamp": 1000000001},
        {"userId": 2, "movieId": 101, "rating": 4.5, "timestamp": 1000000002},
        {"userId": 3, "movieId": 103, "rating": 2.0, "timestamp": 3000000003},
        {"userId": 3, "movieId": 104, "rating": 5.0, "timestamp": 3000000004},
    ]
    

    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as tmpfile:
        tmpfile.write("userId,movieId,rating,timestamp\n") 
        for row in data:
            tmpfile.write(f"{row['userId']},{row['movieId']},{row['rating']},{row['timestamp']}\n")
        return tmpfile.name  

class TestRatings:

    def test_movies_dist_by_year(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings) 
        movies = ratings_obj.Movies(ratings_obj.data)
        результат = movies.dist_by_year()

        assert результат == {2001: 3, 2065: 2}, f"Ожидалось {{2001: 3, 2065: 2}}, но получено {результат}"

    def test_movies_dist_by_rating(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings)  
        movies = ratings_obj.Movies(ratings_obj.data)
        результат = movies.dist_by_rating()

        assert результат == {2.0: 1, 3.5: 1, 4.0: 1, 4.5: 1, 5.0: 1}, f"Ожидалось {{2.0: 1, 3.5: 1, 4.0: 1, 4.5: 1, 5.0: 1}}, но получено {результат}"

    def test_movies_top_by_num_of_ratings(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings) 
        movies = ratings_obj.Movies(ratings_obj.data)
        результат = movies.top_by_num_of_ratings(3)

        assert результат == {101: 2, 102: 1, 103: 1}, f"Ожидалось {{101: 2, 102: 1, 103: 1}}, но получено {результат}"

    def test_movies_top_by_ratings(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings)  
        movies = ratings_obj.Movies(ratings_obj.data)
        результат = movies.top_by_ratings(2, metric=calculate_mean)

        assert результат == {104: 5.0, 101: 4.0}, f"Ожидалось {{104: 5.0, 101: 4.0}}, но получено {результат}"

    def test_users_dist_by_num_of_ratings(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings)  
        users = ratings_obj.Users(ratings_obj.data)
        результат = users.dist_by_num_of_ratings()

        assert результат == {1: 2, 2: 1, 3: 2}, f"Ожидалось {{1: 2, 2: 1, 3: 2}}, но получено {результат}"

    def test_users_top_by_variance(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings) 
        users = ratings_obj.Users(ratings_obj.data)
        результат = users.top_by_variance(1)

        assert результат == {3: 4.5}, f"Ожидалось {{1: 0.25}}, но получено {результат}"

    def test_movies_top_by_controversial(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings) 
        movies = ratings_obj.Movies(ratings_obj.data)
        результат = movies.top_controversial(1)

        assert результат == {101: 0.5}, f"Ожидалось {{101: 0.5}}, но получено {результат}"

    def test_users_dist_by_average_rating(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings)  
        users = ratings_obj.Users(ratings_obj.data)
        результат = users.dist_by_average_rating(metric=calculate_mean)

        assert результат == {1: 3.75, 2: 4.5, 3: 3.5}, f"Ожидалось {{1: 3.75, 2: 4.5, 3: 3.5}}, но получено {результат}"

    def test_movies_top_by_ratings_median(self, sample_ratings):
        ratings_obj = Ratings(sample_ratings)  
        movies = ratings_obj.Movies(ratings_obj.data)
        результат = movies.top_by_ratings(2, metric=calculate_median)

        assert результат == {104: 5.0, 101: 4.0}, f"Ожидалось {{101: 4.0, 104: 5.0}}, но получено {результат}"

