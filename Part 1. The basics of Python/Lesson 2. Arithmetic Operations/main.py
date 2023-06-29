# Сумма
print(1+1)
# Разница
print(1-1)
# Умножение
print(2*2)
# Деление с остатком (float)
print(3/2)
# Деление без остатка
print(5//2)
# Возведение в степень (36)
print(6**2)
# Остаток от деления
print(5 % 2)

# Присвоение переменной какой-либо операции
number = 20
number += 5
number -= 2
number *= 2
number //= 2
number **= 2
number /= 5
print(number) # 105.8

# Работа функции round. После всех операций через запятую принимает число, обозначающее количество цифр после запятой

first_number = 4.95
second_number = 0.00005
print(round(first_number + second_number, 2))
print(round(4.0001 + 0.2, 2))
print(round(4.5))
print(round(4.49))
print(round(4.51))
