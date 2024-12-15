# использование цикла 'for' из предоставленного списка создать список с пролстыми
# и не простыми числами и вывести их на консоль

# дано; список

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]

# создаем новые пустые списки для простых и не простых чисел

primes = []
not_primes = []

# Перебираем числа из списка numbers
for number in numbers:
    # Числа из списка меньше 2 является не простыми и не сложным
    if number < 2:

        continue
    # Считаем число простым, пока не докажем обратное
    is_prime = True

    # Проверяем путем деления в диапазоне от 2 до sqrt(number) + 1
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    # размещаем  число по соответствующем спискам
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Вывод результата
print("Простые числа:", primes)
print("Непростые числа:", not_primes)
