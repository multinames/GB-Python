n = int(input("Введите значение N "))
factorial=1
count=1
for number in range(n):
    factorial=factorial*count
    count+=1
 
print(factorial)
