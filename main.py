from Board import Board
from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer


def playTheGame(humanPlayer, computerPlayer, board):
    current = "X"
    while not board.checkWinner():
        board.display()
        if current == "X":
            indx = humanPlayer.getMove(board)
            board.makeMove(current, indx)
            current ="O"
        else:
            indx = computerPlayer.getMove(board)
            board.makeMove(current, indx)
            current = "X"
    board.display()
    if current == "X":
        print("Computer Player is the Winner.")
    else:
        print("Human Player is the Winner.")
if __name__ == "__main__":
    humanPlayer = HumanPlayer("X")
    computerPlayer = ComputerPlayer("O")
    board = Board()
    playTheGame(humanPlayer, computerPlayer, board)
