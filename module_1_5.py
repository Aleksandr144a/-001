immutable_var = 1,2,3,'alma','mailo','aida'
print(immutable_var)
print(type(immutable_var))
#immutable_var[0] = 6 ошибка - кортеж - неизменяемый тип данных
mutable_var= ([1,2,3], 'alma', 'mailo', 'aida')
print(mutable_var)
print(type(mutable_var))
mutable_var[0][0] = 4
print(mutable_var)


