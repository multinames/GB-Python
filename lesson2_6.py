#Задача 6 на python. Факториал
n = int(input("Введите значение N "))
f, i =  1, 1
if n==0:
    print("1")
else:
    while i <= n:
        f=f*i
        i+=1
    print(f)
