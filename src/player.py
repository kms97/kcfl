
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.calledHands = 0

    def addCard(self, card):
        self.cards.append(card)

    def addCards(self, cards):
        self.cards = cards

    def removeCard(self, card):
        self.cards.remove(card)

    def resetCards(self):
        self.cards = []

    def getCards(self):
        return self.cards

    def getName(self):
        return self.name

    def getCalledHands(self):
        return self.calledHands

    def setCalledHands(self, n):
        self.calledHands = n
