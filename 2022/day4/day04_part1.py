file = open('input.txt', 'r')

total = 0

def processTask(line):
    firstElveRange, secondElveRange = line.split(',')[0], line.split(',')[1]  
    range1 = range(int(firstElveRange.split('-')[0]), int(firstElveRange.split('-')[1]) + 1)
    range2 = range(int(secondElveRange.split('-')[0]), int(secondElveRange.split('-')[1]) + 1)
    
    if range1.start in range2 and range1[-1] in range2 or range2.start in range1 and range2[-1] in range1:
        for i in range1:
            print(i)
    
    return range1.start in range2 and range1[-1] in range2 or range2.start in range1 and range2[-1] in range1

for line in file:
    if( processTask(line.replace('\n', ''))):
        total += 1
    
print(total)