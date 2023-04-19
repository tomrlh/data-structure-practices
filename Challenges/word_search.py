# Given a 2D matrix and a word, identify if this particular word is inside the matrix.

# The word can be constructed from letters that are sequential in adjacent values, where adjacent values
# are those who are horizontally or vertically close by.

# REMEMBER: the same letter cannot be used twice to build a word.

# board = [
# ['A','B','C','E'],
# ['S','F','C','S'],
# ['A','D','E','E']
# ]

# Given the word = "ABCCED", return true.
# Given the word = "SEE", return true.
# Given the word = "ABCB", return false.

# The solution must be implemented inside the function below.
# Tip: You can create other functions and classes if you want but this is the main function that will be used.

########

class MySolution:
    usedLetters = []

    def solution(self, board, word):
        pass

    def searchAround1(self, board, startingPoint: [int]):
        for rIdx, row in board:
            for cIdx, col in row:
                # 1 [x, y], i need to check:
                # top left,             top,                top right
                # [x - 1, y - 1]        [x - 1, y]          [x - 1, y + 1]
                # middle left,          center              middle right
                # [x, y - 1]            [x, y]              [x, y + 1]
                # bottom left,          bottom,             bottom right
                # [x + 1, y - 1]        [x + 1, y]      [x + 1, y + 1]
                # 2 check if value is not used
                # 3 add to used letters and go to next


    def searchAround(self, board, searchFrom: [int], nextLetter):
        row = searchFrom[0]
        col = searchFrom[1]
        valueFound = board[row, col] == nextLetter
        if valueFound != None:
            self.getValue(board, row, col)
            valueFound = self.getTopLeft(board, row, col)
        if valueFound == None:
            valueFound = self.getTop(board, row, col)
        if valueFound == None:
            valueFound = self.getTopRight(board, row, col)
        if valueFound == None:
            valueFound = self.getMiddleLeft(board, row, col)
        if valueFound == None:
            valueFound = self.getMiddleRight(board, row, col)
        if valueFound == None:
            valueFound = self.getBottomLeft(board, row, col)
        if valueFound == None:
            valueFound = self.getBottom(board, row, col)
        if valueFound == None:
            valueFound = self.getBottomRight(board, row, col)


    def getTopLeft(self, board, x, y):
        return self.getValue(board, x-1, y-1)
    def getTop(self, board, x, y):
        return self.getValue(board, x - 1, y)
    def getTopRight(self, board, x, y):
        return self.getValue(board, x - 1, y + 1)
    def getMiddleLeft(self, board, x, y):
        return self.getValue(board, x, y - 1)
    def getMiddleRight(self, board, x, y):
        return self.getValue(board, x, y + 1)
    def getBottomLeft(self, board, x, y):
        return self.getValue(board, x + 1, y - 1)
    def getBottom(self, board, x, y):
        return self.getValue(board, x + 1, y)
    def getBottomRight(self, board, x, y):
        return self.getValue(board, x + 1, y + 1)

    def getValue(self, board, x, y):
        try:
            if board[x, y] != None:
                value = board[x, y]
                self.addUsedLetter(x, y)
                board[x, y] = None
                return value
            else:
                return None
        except IndexError:
            pass

    def addUsedLetter(self, x, y):
        self.usedLetters.append([x,y])