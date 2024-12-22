# задаем глобальную переменную джля посчета вызовов
calls = 0

# создаем функцию для подсчета телефонных звонков
def count_calls():
    global calls
    calls += 1

# Функция, возвращающая информацию о строке
def string_info(string):
    count_calls() #Увеличиваем счетчик вызовов
    return len(string), string.upper(), string.lower()

#Функция, проверяющая наличие строки в списке (без учета регистра)
def is_contains(string, list_to_search):
    count_calls() # Увеличиваем счетчик вызовов
    string_lower = string.lower( ) # поиводим строку к нижнему регистру
    list_lower = [item.lower() for item in list_to_search]  # Приводим элементы
    return string_lower in list_lower

# Вызов функции с произвольными данными
print(string_info('Capybara')) #(8,'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  #(10, 'ARMAGEDDON', 'armageddon')

print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))  #True
print(is_contains('cycle', ['trecycling', 'cyclic']))  #False

#вывод олбщего количества выззховов функции
print(calls)

