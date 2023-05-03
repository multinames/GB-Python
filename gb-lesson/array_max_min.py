# Нахождение индексов максимального и минимального элемента массива (16)
import random
current = list(range(16))
random.shuffle(current)
print("Элементы массива", current)
n = len(current)
min_index = 0
i = 0
max_el = current[0]
min_el = current[0]
while i < n:
    if max_el < current[i]:
        max_el = current[i]
        max_index = i
    elif min_el > current[i]:
        min_el = current[i]
        min_index = i
    i += 1
print("Максимальный элемент -", max_el, "индекс максимального элемента -", max_index)
print("Минимальный элемент -", min_el, "индекс минимального элемента -", min_index)
