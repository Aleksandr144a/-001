# Задаем функцию, которая будет перебирать все элементы, проверять их тип
# и подсчитывать сумму чисел и длину строк

def calculate_structure_sum(data):
    total = 0

    # Если элемент - число, добавляем его к сумме
    if isinstance(data, (int, float)):
        return data

    # Если элемент - строка, добавляем длину строки
    elif isinstance(data, str):
        return len(data)

    # Если элемент - список, кортеж или множество, обрабатываем элементы
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += calculate_structure_sum(item)

    # Если элемент - словарь, обрабатываем ключи и значения
    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    # Возвращаем сумму для текущего элемента
    return total

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
