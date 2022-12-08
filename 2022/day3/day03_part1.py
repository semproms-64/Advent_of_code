from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
length_al = len(LETTERS)
file = open('input.txt', 'r')
totalValue = 0

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)


def processRucksack(line):
    half = len(line)//2

    fCompartiment = slice(0,half)
    sCompartiment = slice(half, len(line))
    
    commonLetters = set(str(line[fCompartiment])).intersection(str(line[sCompartiment]))
    letter = str(list(commonLetters)[0])
    
    if letter.isupper():
        value = int(alphabet_position(letter)) + length_al
    else:
        value = int(alphabet_position(letter))
        
    return value

for line in file:
    totalValue += processRucksack(line)
    
print(totalValue)