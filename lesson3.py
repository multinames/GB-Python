numbers =[1, 8, 3, 2, 6]
size = 5
first = numbers[0]
second= numbers[0]
print("Шаг 1", first, second)
if (numbers[1] > first):
    print(first, second)
    first=numbers[1]
else:
    second=numbers[1]
current_index=2
while (current_index <size):
    print(first, second)
    if(numbers[current_index] > first):
        second=first
        first=numbers[current_index]
    else:
        if(numbers[current_index] > second):
            second= numbers[current_index]
    current_index+=1
print(second)

        
