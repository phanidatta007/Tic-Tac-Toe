import random
from Player import Player


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def getMove(self, board):
        move = None
        valid = False
        while not valid:
            move = random.randint(0,8)
            valid = board.checkValid(move)
        return move

