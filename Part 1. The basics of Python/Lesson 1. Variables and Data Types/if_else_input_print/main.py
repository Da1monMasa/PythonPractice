

'''
Выяснение типа переменной
'''

userId = "abc"  # тип str
print(type(userId))  # <class 'str'>

userId = 234  # тип int
print(type(userId))  # <class 'int'>

userId = 1.5
print(type(userId)) # <class 'float'>

userId = True
print(type(userId)) # <class 'bool'>


'''
Input, print test.
if\else test
использование "f", вставка значений определённой переменной в строку

'''

first_name = input("Enter your First Name:")
middle_name = input("Enter your Middle Name:")
last_name = input("Enter your Last Name if it exist:")
if(last_name == None):
    username = f"\n{first_name} \n{middle_name}"
    print(username)
else:
    username = f"\n{first_name} \n{middle_name} \n{last_name}"
    print(username)
'''
Из-за символов \n например путь к файлу будет отображаться некорректно, 
поэтому используется символ r, чтобы избежать подобной ситуации
'''
print("Некорректное отображение:", end = " ")
path = "C:\python\name.txt"
print(path)

print("Корректное отображение:", end = " ")
path = r"C:\python\name.txt"
print(path)
