file = open('input.txt', 'r')

def processingMessage(elements, size):
    counter = size
    
    for i in range(len(elements)):
        if len(set(elements[i:i+size])) != size:
            counter += 1
        else:
            break
    return counter


for line in file:
    print(processingMessage(line, 14))