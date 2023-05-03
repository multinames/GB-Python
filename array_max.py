import random
current = list(range(16))
#current = random.randint(0, 16)
print(current)
#current =  [6, 12, 4, 3, 8]
max_index=0
n=len(current)
i=0
max = current[0]
while (i < n):
    if max < current[i]:
        max = current[i]
        max_index=i
    i+=1
print("Максимальный элемент -", max, "индекс максимального элемента -", max_index)

    