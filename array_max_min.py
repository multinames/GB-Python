#Нахождение индексов максимального и минимального элемента массива (16)
import random
current = list(range(16))
random.shuffle(current)
print("Элементы массива", current)
n=len(current)
i=0
max = current[0]
min = current[0]
while (i < n):
    if max < current[i]:
        max = current[i]
        max_index=i
    elif min > current[i]:
        min = current[i]
        min_index=i
    i+=1
print("Максимальный элемент -", max, "индекс максимального элемента -", max_index)
print("Минимальнй элемент -", min, "индекс минимального элемента -", min_index)



    