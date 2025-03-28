import sys

def read_population_data(file_path):
    """
    Зчитує дані з файлу та повертає список словників.
    Формат кожного рядка: "назва країни, площа, населення"
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    country, area, population = [item.strip() for item in line.split(',')]
                    # Перетворення даних на відповідні типи
                    area = float(area)
                    population = int(population)
                    data.append({
                        'country': country,
                        'area': area,
                        'population': population
                    })
                except ValueError as e:
                    print(f"Помилка обробки рядка: {line}. Помилка: {e}", file=sys.stderr)
    return data

def sort_by_area(data):
    """Сортує дані за площею (від меншої до більшої)"""
    return sorted(data, key=lambda x: x['area'])

def sort_by_population(data):
    """Сортує дані за населенням (від меншої до більшої)"""
    return sorted(data, key=lambda x: x['population'])