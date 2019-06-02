class rules:
    def __init__(self, allCards):
        self.allCards = allCards
        self.isGameOver()

    def isGameOver(self):
        playerPoints = 0
        dealerPoints = 0

        for i in range(len(self.allCards['player'])):
            playerPoints = playerPoints + self.allCards['player'][i]['points']
        for i in range(len(self.allCards['dealer'])):
            dealerPoints = dealerPoints + self.allCards['dealer'][i]['points']          
       
        if playerPoints >= 21:
            return True
        if dealerPoints >= 17:
            return True 
        return False