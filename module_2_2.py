# Вводим числа
first = int(input('Введите число первое: '))
second = int(input('Введите число второе : '))
third = int(input('Введите число третье'))

# Задаем услдовие
if first == second == third:
    print(3) # все введенные числа равны
elif first == second or first == third or second == third:
    print(2) # только два введенных числа равны
else :
    print(0) #все введенные равны