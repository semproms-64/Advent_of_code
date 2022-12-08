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
    
    if (player1 == 'A' and player2 == 'X') or (player1 == 'B' and player2 == 'Y') or (player1 == 'C' and player2 == 'Z'):
        points = dictionary_player[player2] + 3 #Case draw
    elif (player1 == 'A' and player2 == 'Y') or (player1 == 'B' and player2 == 'Z') or (player1 == 'C' and player2 == 'X'):
        points = dictionary_player[player2] + 6 #Case win
    else:
        points = dictionary_player[player2] + 0 #Case lose
        
    return points

        
    

for line in file:
    totalPoints += getResultRound(line)
    
print(totalPoints)