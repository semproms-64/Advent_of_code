file = open('input.txt', 'r')
totalPoints = 0

dictionary_player = {
    'X' : 1, #Rock A
    'Y' : 2, #Paper B
    'Z' : 3,  #Scissors C
}

def getResultRound(chain):
    player1, player2 = chain.split()[0], chain.split()[1]
    points = 0
    
    if player2 == 'X': #Lose
        if player1 == 'A':
            points = dictionary_player['Z'] + 0
        elif player1 == 'B':
            points = dictionary_player['X'] + 0
        else:
            points = dictionary_player['Y'] + 0
    elif player2 == 'Y': #Draw
        if player1 == 'A':
            points = dictionary_player['X'] + 3
        elif player1 == 'B':
            points = dictionary_player['Y'] + 3
        else:
            points = dictionary_player['Z'] + 3
    else: #Win
        if player1 == 'A':
            points = dictionary_player['Y'] + 6
        elif player1 == 'B':
            points = dictionary_player['Z'] + 6
        else:
            points = dictionary_player['X'] + 6
    
        
    return points

        
    

for line in file:
    totalPoints += getResultRound(line)
    
print(totalPoints)