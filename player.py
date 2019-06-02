import sys
class player:
    def __init__(self, allCards, playerCredit):
        self.allCards = allCards
        self.playerCredit = playerCredit
    
    def playerTurn(self):
        print('player')