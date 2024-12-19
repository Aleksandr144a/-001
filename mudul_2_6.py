
#задаем функцию
def generate_password(n):
    # Задаем условие для проверки вводимогочислв
    if not (3 <= n <= 20):
        return 'Число должно быть в диапазоне от 3 до 20'
    result = ''
# Задаем внешний цикл
    for i in range(1, n):
        # Задаем внутренний цикл для исключения повторения пар
        for j in range(i, n):
            # Задаем условие ждля уникальных пар
            pair_sum = i + j
            if n % pair_sum == 0 and i != j:
                # Формируем пары
                result += str(i) + str(j)

    return result

n = int(input('Введите число от 3 до 20 :'))
password = generate_password(n)
print(f'Нужный пароль: {password}')
