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
