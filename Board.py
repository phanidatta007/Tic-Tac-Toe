class Board:
    def __init__(self):
        self.places = []
        for i in range(9):
            self.places.append(" ")
    def makeMove(self, letter, index):
        if self.places[index] == " ":
            self.places[index] = letter
            return True
        return False
    def checkValid(self, index):
        if self.places[index] == " ":
            return True
        return False
    def checkWinner(self):
        if (self.places[0] == self.places[1] == self.places[2] != " ") or \
            (self.places[3] == self.places[4] == self.places[5] != " ") or \
                (self.places[6] == self.places[7] == self.places[8] != " "):
            return True
        elif (self.places[0] == self.places[3] == self.places[6] != " ") or \
                (self.places[1] == self.places[4] == self.places[7] != " ") or \
                (self.places[2] == self.places[5] == self.places[8] != " "):
            return True
        elif (self.places[0] == self.places[4] == self.places[8] != " ") or \
                (self.places[2] == self.places[4] == self.places[6] != " "):
            return True
        return False
    def display(self):
        print("{}|{}|{}".format(self.places[0],self.places[1],self.places[2]))
        print("{}|{}|{}".format(self.places[3],self.places[4],self.places[5]))
        print("{}|{}|{}".format(self.places[6],self.places[7],self.places[8]))
        print()

