# задаем функцию с тремя переменными
def get_matrix(n, m, value):
    # создаем список пусто для формирования матрицы
    matrix = []
    # цикл для формирования строк матрицы размером n
    for i in range(n):
        # пустой список для текущей строки
        row = []
        #внутренний цикл для формирования столбцов матрицы размером m

        for j in range(m):
            # добавляем значение в строку
            row.append(value)
        # добавляем строку в матрицу
        matrix.append(row)
        # возвращаем готовую матрицу
    return matrix

# использование функции

result1 = get_matrix(2, 5, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 4, 13)

# вывод результата

print(result1)
print(result2)
print(result3)