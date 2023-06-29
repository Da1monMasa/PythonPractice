# Variables and Data Types

Variables
Variables are used to store data. In Python, variable names must start with an alphabetic character or an underscore and can contain alphanumeric characters and underscores. Additionally, variable names should not match the names of Python's keywords. There are not many keywords, and they are easy to remember:


|  var name    | var name     | var name      |  var name      | var name     |
|------|------|-------|--------|------|
| False | await | else  | import | pass |
| None | break | except | in | raise |
| True | class | finally | is | return |
| and | continue | for | lambda | try |
| as | def | from | nonlocal | while |
| assert | del | global | not | with |
| async | elif | if | or | yield |


A variable stores data of one of the data types. In Python, there are several different data types. In this case, let's consider only the most basic types

1. **bool**
2. **int**
3. **float**
4. **complex**
5. **str**.


### bool
```

isMarried = False
print(isMarried)    # False
 
isAlive = True
print(isAlive)      # True
```

### Целые числа

Тип int представляет целое число, например, 1, 4, 8, 50. Пример
```
age = 21
print("Возраст:", age)    # Возраст: 21
 
count = 15
print("Количество:", count) # Количество: 15
```
### Дробные числа
Тип float представляет число с плавающей точкой, например, 1.2 или 34.76. В качесте разделителя целой и дробной частей используется точка.
```
height = 1.68
pi = 3.14
weight = 68.
print(height)   # 1.68
print(pi)       # 3.14
print(weight)   # 68.0
```

### Строки
Тип str представляет строки. Строка представляет последовательность символов, заключенную в одинарные или двойные кавычки, например "hello" и 'hello'. В Python 3.x строки представляют набор символов в кодировке Unicode
```
message = "Hello World!"
print(message)  # Hello World!
 
name = 'Tom'
print(name)  # Tom
```

Управляющие последовательности в строке
Строка может содержать ряд специальных символов - управляющих последовательностей. Некоторые из них:

* \\: позволяет добавить внутрь строки слеш

* \': позволяет добавить внутрь строки одинарную кавычку

* \": позволяет добавить внутрь строки двойную кавычку

* \n: осуществляет переход на новую строку

* \t: добавляет табуляцию (4 отступа)
