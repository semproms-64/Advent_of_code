file = open('input.txt', 'r')
max = 0
suma = 0

for line in file:
    if line != '\n':
        suma += int(line)
    else:
        if suma > max:
            max = suma
        suma = 0
        
print(max)

