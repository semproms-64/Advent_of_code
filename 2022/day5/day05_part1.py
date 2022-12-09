with open('input.txt') as file:
    stack, instructions = (element.splitlines() for element in file.read().strip('\n').split('\n\n'))

def displayStacks():
    for stack in stacks:
        print(stack, stacks[stack])
        
def loadStacks():
    for string in stack[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1
            
        
def processInstructions():
    for instruction in instructions:
        quantity = int(instruction.split("move")[1].split("from")[0])
        from_stack = int(instruction.split("move")[1].split("from")[1].split("to")[0])
        to_stack = int(instruction.split("move")[1].split("from")[1].split("to")[1])  
        moveStack(from_stack, to_stack, quantity)
                
def moveStack(from_stack, to_stack, quantity):
    index = 0
    
    while index < quantity:
        element = stacks[from_stack].pop()
        stacks[to_stack].append(element)
        index += 1
    
def getSolution():
    solution = ''
    for stack in stacks:
        solution += stacks[stack].pop()
        
    return solution

stacks = {int(digit):[] for digit in stack[-1].replace(" ", "")}
indexes = [index for index, char in enumerate(stack[-1]) if char != " "]
loadStacks()
displayStacks()
print()
processInstructions()
print('After processing')
print()
displayStacks()
print(getSolution())
