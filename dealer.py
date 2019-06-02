import sys
class dealer:
    def __init__(self, allCards):
        self.allCards = allCards
    
    def isDraw(self):
        total = 0
        for i in self.allCards:
            total = total + i['points']
        if total < 17:
            return True
        else: return False
    
    def getWinner(self):
        totalPlayer = 0
        totalDealer = 0
        winner = ''
        for i in range(len(self.allCards['player'])):
            totalPlayer = totalPlayer + self.allCards['player'][i]['points']    
        for i in range(len(self.allCards['dealer'])):
            totalDealer = totalDealer + self.allCards['dealer'][i]['points']  
        if (totalPlayer <= 21 and totalPlayer > totalDealer and totalDealer <= 21) or (totalDealer > 21 and totalPlayer <=21) or (totalDealer == totalPlayer):
            if totalDealer == totalPlayer:
                return 'split'
            else: return 'player'
        else: return 'dealer'
        
        return winner