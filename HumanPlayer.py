from Player import Player


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, board):
        move = None
        valid = False
        while not valid:
            move = int(input("Enter The Number Between 0-8: "))
            valid = board.checkValid(move)
        return move
