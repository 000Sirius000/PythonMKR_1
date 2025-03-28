import os
import tempfile
import pytest
from population_sorter import read_population_data, sort_by_area, sort_by_population

# Фікстура для створення тимчасового файлу з тестовими даними
@pytest.fixture
def sample_data_file():
    data = """Україна, 603700, 42000000
Франція, 551695, 67000000
Німеччина, 357022, 83000000
Італія, 301340, 60000000
"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as tmp:
        tmp.write(data)
        tmp_path = tmp.name
    yield tmp_path
    os.remove(tmp_path)

# Тест зчитування даних з файлу
def test_read_population_data(sample_data_file):
    data = read_population_data(sample_data_file)
    assert len(data) == 4
    # Перевірка типів даних
    for item in data:
        assert isinstance(item['country'], str)
        assert isinstance(item['area'], float)
        assert isinstance(item['population'], int)

# Параметризований тест для сортування за площею
@pytest.mark.parametrize("input_data, expected_first_country", [
    (
        [
            {'country': 'КраїнаA', 'area': 500, 'population': 1000},
            {'country': 'КраїнаB', 'area': 300, 'population': 2000},
            {'country': 'КраїнаC', 'area': 700, 'population': 1500},
        ],
        'КраїнаB'
    ),
    (
        [
            {'country': 'КраїнаX', 'area': 1000, 'population': 5000},
            {'country': 'КраїнаY', 'area': 800, 'population': 3000},
        ],
        'КраїнаY'
    )
])
def test_sort_by_area(input_data, expected_first_country):
    sorted_data = sort_by_area(input_data)
    assert sorted_data[0]['country'] == expected_first_country

# Параметризований тест для сортування за населенням
@pytest.mark.parametrize("input_data, expected_first_country", [
    (
        [
            {'country': 'КраїнаA', 'area': 500, 'population': 3000},
            {'country': 'КраїнаB', 'area': 300, 'population': 1000},
            {'country': 'КраїнаC', 'area': 700, 'population': 2000},
        ],
        'КраїнаB'
    ),
    (
        [
            {'country': 'КраїнаX', 'area': 1000, 'population': 8000},
            {'country': 'КраїнаY', 'area': 800, 'population': 6000},
        ],
        'КраїнаY'
    )
])
def test_sort_by_population(input_data, expected_first_country):
    sorted_data = sort_by_population(input_data)
    assert sorted_data[0]['country'] == expected_first_country