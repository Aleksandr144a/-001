#Создайте новый проект в PyCharm

#Создайте  функцию test_function
#Создайте ввложенную функцию - inner_function, она выводит печатать значение "Я в области видимости функции test_function"

def test_function():
    # Вложенная функция
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов вложенной функции
    inner_function()


# Вызов test_function
test_function()

# Попробуем вызвать inner_function вне област видимостиtest_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")