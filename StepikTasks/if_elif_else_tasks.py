
# Задание про норму сна. Если количество часов для сна Ани 
#больше либо равно норме и это же количество часов меньше либо 
#равно В, программа говорит что "Это нормально". 
#В остальных случая срабатывают конструкции elif


A = int(input())
B = int(input())
H = int(input())

if(H >= A and H <= B):
    print("Это нормально")
elif(H >= A):
    print("Пересып")
elif(H <= A):
    print("Недосып")
