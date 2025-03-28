import sys


def read_population_data(file_path):
    """
    Зчитує дані з файлу та повертає список словників .
    Формат кожного рядка: "назва країни, площа, населення"
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    country, area, population = [item.strip() for item in line.split(',')]
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


def main():
    # Якщо не передано аргументів, використати data.txt за замовчуванням
    file_path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"

    try:
        data = read_population_data(file_path)
    except FileNotFoundError:
        print(
            f"Файл '{file_path}' не знайдено. Будь ласка, переконайтесь, що файл існує у кореневій директорії проєкту.")
        sys.exit(1)

    sorted_area = sort_by_area(data)
    sorted_population = sort_by_population(data)

    print("Сортування за площею:")
    for item in sorted_area:
        print(f"{item['country']}: {item['area']}")

    print("\nСортування за населенням:")
    for item in sorted_population:
        print(f"{item['country']}: {item['population']}")


if __name__ == '__main__':
    main()