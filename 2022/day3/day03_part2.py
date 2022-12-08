from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
length_al = len(LETTERS)
file = open('input.txt', 'r')
totalValue = 0

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    print(numbers)
    return ' '.join(numbers)

def processRucksack(line1, line2, line3):
    set1, set2, set3 = set(line1), set(line2), set(line3)
    commonLetter = str(set1.intersection(set2).intersection(set3))
    
    if commonLetter.isupper():
        value = int(alphabet_position(commonLetter)) + length_al
    else:
        value = int(alphabet_position(commonLetter))
    
    return value

index = 0

for line in file:
    line1 = line.replace("\n", "")
    line2 = file.readline().replace("\n", "")
    line3 = file.readline().replace("\n", "")
    
    totalValue += processRucksack(line1, line2, line3)
    
print(totalValue)