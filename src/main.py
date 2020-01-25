from player import Player
from board import Board
from card import Card
import random
import pygame

board = Board()
window =  pygame.display.set_mode((500,500))
pygame.display.set_caption("Client")
clientNumber = 0

def redrawWindow():
    window.fill((255,255,255))
    pygame.diplay.update()

def addPlayer(name):
    p = Player(name)
    board.addPlayer(p)

def printCardsofPlayer(name):
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

    # print("Round 1")
    # board.distributeCards()
    # printCardsofPlayer("Player 1")
    # printCardsofPlayer("Player 2")
    # board.resetCards()
    # print("Round 2")
    # board.distributeCards()
    # printCardsofPlayer("Player 1")
    # printCardsofPlayer("Player 2")
    # board.resetCards()
    # print("Round 3")
    # board.distributeCards()
    # printCardsofPlayer("Player 1")
    # printCardsofPlayer("Player 2")
    # board.resetCards()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        #redrawWindow()


    