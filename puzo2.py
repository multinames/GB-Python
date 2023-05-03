#https://otus.ru/journal/puzyrkovaya-sortirovka-na-python-i-s/
current =  [1, 8, 3, 8, 6]
j=0
print("Начальный массив", current)
n=len(current)
for i in range(n):
 
    for j in range(0, n-i-1):
        if current[j] > current[j+1]:
            max=current[j]
            current[j] = current[j+1]
            current[j+1]=max  
        j+=1
        
    i+=1
print("Отсортированный массив", current)
i=0
while (current[i] < max):
   i+=1
print (current[i])


  

    
