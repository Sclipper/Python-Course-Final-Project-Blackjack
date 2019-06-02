import os

import player
from dealer import dealer
from rules import rules
import text

import json
from random import randint
clear = lambda: os.system('cls')
class GameInit:
    
    def __init__(self, rules, player, dealer, decksCount, playerCredit, allCards, deck):
        self.rules = rules
        self.player = player
        self.dealer = dealer
        self.decksCount = decksCount
        self.bet = 0
        self.playerChoice = ''
        self.isSplit = False
        self.playerCredit = playerCredit
        self.allCards = allCards
        self.deck = deck
        self.usedCards = []
        self.play()

    def play(self):
        while self.playerComunication(text.playP, text.playI) != 'no' and self.playerCredit != 0:
            self.resetGameState()
            self.bet = self.playerComunication('', text.layBetsI)

            while int(self.bet) > int(self.playerCredit) and self.bet.isdigit() :
                self.bet = self.playerComunication('', text.layBetsErrorI)
            self.playerCredit = int(self.playerCredit) - int(self.bet)
            self.drawCards('start')

            while not self.rules(self.allCards).isGameOver():
                if self.playerChoice != 'stand':
                    self.playerChoice = self.playerComunication(text.playerChoiceP, text.playerChoiceI).lower().strip()
                    while self.playerChoice not in ['hit', 'stand']:
                        self.playerChoice = self.playerComunication(text.validOptionP, text.playerChoiceI).lower().strip()
                
                self.drawCards(f'{self.playerChoice}')
            winner = self.dealer(self.allCards).getWinner()
            if winner == 'player':
                self.playerCredit = int(self.bet) * 2 + int(self.playerCredit)
                print(f'\nPlayer wins!  Credits remaning: {self.playerCredit}')
            if winner == 'dealer':
                print(f'\nDealer wins!  Credits remaning: {self.playerCredit}')
            if winner == 'split':
                self.playerCredit = int(self.bet) + int(self.playerCredit)
                print(f'\nSplit!  Credits remaning: {self.playerCredit}')
            if int(self.playerCredit) == 0:
                self.playerCredit = self.playerComunication('', text.addMoreCredits)
                if not self.playerCredit.isdigit():
                    break
        
    def drawCards(self, action): 
        if action == 'start':
            self.getRandomCards('dealer', 1)
            self.getRandomCards('player' ,2)
        if action == 'hit':
            self.getRandomCards('player', 1)
        if action == 'stand':
            if self.dealer(self.allCards['dealer']).isDraw():
                self.getRandomCards('dealer',1)
        self.drawBoard()
    
    # Draws a random card from the remaning deck
    def getRandomCards(self, owner, amount):
        arr =[]
        for i in range(amount):
            temp = randint(0, 51 * int(self.decksCount))
            while temp in self.usedCards:
                temp = randint(0, 51 * int(self.decksCount))
            self.usedCards.append(temp)
            if temp > 51 and temp < 102:
                arr.append(temp - 51)
            if temp > 102:
                arr.append(temp - 102)
            if temp <= 51 :
                arr.append(temp)
        for i in range(len(arr)):
            self.allCards[owner].append(deck[arr[i]]) 

    def drawBoard(self):
        clear()
        print('Dealer cards')
        total = 0 
        for i in range(len(self.allCards['dealer'])):
            total = total + self.allCards['dealer'][i]['points']
            print(end = self.allCards['dealer'][i]['text'])
        print(f'   Total points: {total}')
        total = 0
        print('Player cards')
        for i in range(len(self.allCards['player'])):
            total = total + self.allCards['player'][i]['points']
            print(end = self.allCards['player'][i]['text'])
        print(f'   Total points: {total}')
        print(f'   \nBet: {self.bet}   Credits: {self.playerCredit}')

    def playerComunication(self, text, playerResponse):
        if text != '':
            print(text)
        return input(playerResponse)

    def resetGameState(self): 
        self.allCards = {"player": [], "dealer": []}
        self.bet = 0
        self.playerChoice = ''
        if len(self.usedCards) > 30 * int(self.decksCount) :
            print('Shufling....')
            self.usedCards = []

# Initial preparations
deck = {}
with open('deck.json') as f:
    deck = json.load(f)
allCards = {"player": [], "dealer": []}
clear()
print(text.welcomeP)
print(text.decksAmountP)
decksCount = input(text.decksAmountI)   

while int(decksCount) > 3 or int(decksCount) <= 0:
    if int(decksCount) > 3:
        decksCount = input(text.smallerI)
    else:
        decksCount = input(text.biggerI)
playerCredit = input(text.addCreditsI)
while not playerCredit.isdigit():
    playerCredit = input(text.addCreditsE)

GameInit(rules, player, dealer, decksCount, playerCredit, allCards, deck)
