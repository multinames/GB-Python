import random
current = list(range(16))
#current = random.randint(0, 16)
print(current)
#current =  [6, 12, 4, 3, 8]
max_index = 0
n = len(current)
i = 0
max_el = current[0]
while i < n:
    if max_el < current[i]:
        max_el = current[i]
        max_index=i
    i += 1
print("Максимальный элемент -", max_el, "индекс максимального элемента -", max_index)

    