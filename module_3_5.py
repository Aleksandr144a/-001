# Задаем функцию
def get_multiplied_digits(number):
    # Преобразуем число в строку для удобства работы с отдельными цифрами
    str_number = str(number)

    # Определяем первую цифру числа
    first = int(str_number[0])

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:5]))
    else:
        # Базовый случай: если осталась одна цифра, возвращаем её
        return first

# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Вывод: 24



