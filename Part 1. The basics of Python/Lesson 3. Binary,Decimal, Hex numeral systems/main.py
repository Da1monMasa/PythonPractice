'''
 Операции с данными
'''

# Сумма, разница, произведение, деление, целочисленное деление, возведение в степень, получение остатка от деления

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

number = 20
number += 5
number -= 2
number *= 2
number //= 2
number **= 2
number /= 5
print(number) # 105.8

first_number = 4.95
second_number = 0.00005
print(round(first_number + second_number, 2))
print(round(4.0001 + 0.2, 2))
print(round(4.5))
print(round(4.49))
print(round(4.51))

print("Десятичное число в двоичной системе счисления:")
number_ten0 = 10
number_ten1 = 0b10110
number_ten2 = 0o10110
number_ten3 = 0x10110
decimal_number = 22
hexadecimal_number = hex(decimal_number)
print(hexadecimal_number)
print(number_ten1)
print(number_ten2)
print(number_ten3)
print(f"number = {number_ten0:0b}") # 1010
print("Десятичное число в восьмиричной системе счисления:")
print(f"number = {number_ten0:0o}") # 12
print("Десятичное число в шестнадцатиричной системе счисления:")
print(f"number = {number_ten0:0x}") #a
