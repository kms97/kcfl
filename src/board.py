
from player import Player
from card import Card
import random

class Board:
    def __init__(self):
        self.playerList = []
        suits = ["Spade", "Heart", "Diamond", "Club"]
        self.deck = [Card(suit, value) for value in range(1, 14) for suit in suits]
        self.maxCards = 0
        self.round = 1  
        self.maxRounds = 1      

    def addPlayer(self, player):
        self.playerList.append(player)
        self.maxRounds = 52 // len(self.playerList)

    def removePlayer(self, player):
        self.playerList.remove(player)

    def getPlayerNames(self):
        for p in self.playerList:
            print(p.getName())
    
    def getPlayerByName(self, name):
        for p in self.playerList:
            if p.name == name: return p
        return None

    def getDeck(self):
        return self.deck
    
    def printDeck(self, deck):
        for d in deck:
            print(d.value, d.suit)

    def randomiseDeck(self):
        random.shuffle(self.deck)

    def distributeCards(self):
        self.randomiseDeck()
        self.randomiseDeck()
        self.randomiseDeck()
        self.randomiseDeck()
        self.randomiseDeck()
        numPlayers = len(self.playerList)
        numCardsToUse = self.round * numPlayers
        j = 0
        for i in range(numCardsToUse):
            p = self.playerList[j]
            p.addCard(self.deck[i])
            j = j + 1
            if j == numPlayers: j = 0
        if self.round < self.maxRounds: self.round = self.round + 1
        else: self.round = 1

    def resetCards(self):
        for p in self.playerList:
            p.resetCards()
    
        


        