file = open('input.txt', 'r')
max = 0
suma = 0
array = []

for line in file:
    if line != '\n':
        suma += int(line)
    else:
        array.append(suma)
        suma = 0
        
array.sort()

print(array[len(array)-1] + array[len(array)-2] + array[len(array)-3])

