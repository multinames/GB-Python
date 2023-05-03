# Урок 2. Задание на «разворот» массива
import random
current = list(range(16))
random.shuffle(current)
n=len(current)
mirror = [0 for i in range(n)]
i =0
print("Исходный массив", current)
while (i < len(current)) :
    mirror[i]=current[n-1]
    i=i+1
    n=n-1
(print("Перевернутый массив", mirror))