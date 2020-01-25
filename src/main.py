from player import Player
from board import Board
from card import Card
import random

board = Board()



def addPlayer(name):
    p = Player(name)
    board.addPlayer(p)

def printCards(name):
    p = board.getPlayerByName(name)
    if p is None:
        print("Player not found")
        return
    print(p.getName())
    cards = p.getCards()
    for c in cards:
        print(c.value, c.suit)

if __name__ == '__main__':
    print("Adding players")
    addPlayer("Player 1")
    addPlayer("Player 2")
    addPlayer("Player 3")
    addPlayer("Player 4")
    board.getPlayerNames()
    board.randomiseDeck()

    print("Round 1")
    board.distributeCards()
    printCards("Player 1")
    printCards("Player 2")
    board.resetCards()
    print("Round 2")
    board.distributeCards()
    printCards("Player 1")
    printCards("Player 2")
    board.resetCards()
    print("Round 3")
    board.distributeCards()
    printCards("Player 1")
    printCards("Player 2")
    board.resetCards()
    


    