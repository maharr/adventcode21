import numpy as np

class bingoBoard:
    def __init__(self, numbers):
        self.numbers = np.array(numbers)
        self.winner = -1
    
    def check(self, number):
        if number in self.numbers and self.winner == -1:
            index = np.where(number == self.numbers)
            self.numbers[index] = -1
            if -5 in self.numbers.sum(axis=0):
                self.winner = self.numbers[self.numbers >= 0].sum() * number
                return True
            if -5 in self.numbers.sum(axis=1):
                self.winner = self.numbers[self.numbers >= 0].sum() * number
                return True
            return False
        return False

def findWinner(calls,boards):
    winner = -1
    last = -1
    for call in calls:
        for board in boards:
            if board.check(call):
                print(board.winner)
                if winner == -1 :
                    winner = board.winner
                else:
                    last = board.winner
    return winner, last



with open("4/input.txt", "r") as f:
    calls = [ int(x) for x in f.readline().split(",") ]
    lines = f.read().splitlines()

boards = []

for i in range(1,len(lines),6):
    numbers = []
    for j in range(5):
        numbers.append([ int(x) for x in lines[i+j].split()])
    boards.append(bingoBoard(numbers))

winner, last = findWinner(calls,boards)
print("First winning board is ", winner)
print("The last winning board is ", last)

            




