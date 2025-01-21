import pytest
from unittest.mock import mock_open, patch
from movielens_analysis import Tags

@pytest.fixture
def mock_tag_data():
    return (
        "userId,movieId,tag,timestamp\n"
        "1,1,amazing movie,123456\n"
        "2,1,beautiful film,123457\n"
        "3,2,great action movie,123458\n"
        "4,2,awesome,123459\n"
        "5,3,life changing,123460\n"
        "6,3,inspirational,123461\n"
        "7,4,funny comedy,123462\n"
    )

@pytest.fixture
def tags(mock_tag_data):
    with patch("builtins.open", mock_open(read_data=mock_tag_data)):
        yield Tags("tags.csv")

class TestTags:

    def test_most_words(self, tags):
        expected = {'amazing movie': 2, 'beautiful film': 2, 'great action movie': 3}
        result = tags.most_words(3)
        assert result == expected


    def test_longest(self, tags):
        expected = ["great action movie", "beautiful film", "amazing movie"]
        result = tags.longest(3)
        assert result == expected

    def test_most_words_and_longest(self, tags):
        result = tags.most_words_and_longest(2)
        assert "great action movie" in result

    def test_most_popular(self, tags):
        expected = {"amazing movie": 1, "beautiful film": 1, 'funny comedy': 1, 
                    "great action movie": 1, "awesome": 1, "life changing": 1, 
                    "inspirational": 1}
        result = tags.most_popular(7)
        assert result == expected

    def test_tags_with(self, tags):
        result = tags.tags_with("movie")
        assert result == ["amazing movie", "great action movie"]