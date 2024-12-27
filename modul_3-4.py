
    # Решение с использованием опкратора count
    # Задаем функцию с двумя пкременными


def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word_lower = root_word.lower()
    # Создаем пустой список для результатов
    same_words = []

    for word in other_words:
        # Приводим каждое слово к нижнему регистру для сравнения
        word_lower = word.lower()
        # Проверяем, если одно слово содержится в другом
        if root_word_lower.count(word_lower) > 0 or word_lower.count(root_word_lower) > 0:
            same_words.append(word)  # Добавляем исходное слово в список

    # Возвращаем результирующий список
    return same_words
    # Тестируем функцию


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # ['richiest', 'orichalcum', 'richies']print(result2)  # ['Able', 'Disable']\
print(result2)  # ['Able', 'Disable']


# Решение с использованием опкратора if
# Задаем функцию с двумя пкременными

def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для корректного сравнения
    root_word_lower = root_word.lower()

    # Создаем список для хранения подходящих слов
    same_words = []

    # Перебираем каждое слово из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержится ли одно слово в другом
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем результирующий список
    return same_words


# Пример использования функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на экран
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
