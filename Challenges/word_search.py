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

################################################################################################################

class MySolution:
    usedLetters = []

    def solution(self, board, word):
        found_letters_positions = []
        first_letter_position = MySolution.find_letter(board, word[0])  # the first because will not search around it
        if first_letter_position is not None:
            print("first letter found: {}".format(board[first_letter_position[0]][first_letter_position[1]]))
            found_letters_positions.append(first_letter_position)
            for letter in word[1:]:
                search_from = None
                if len(found_letters_positions) > 0:
                    search_from = found_letters_positions[-1]
                else:
                    search_from = first_letter_position
                next_letter_position = self.search_around(self, board, search_from, letter)
                print("next letter position: {}".format(next_letter_position))
                if next_letter_position is not None:
                    print("letter found: {}, in the position: {} ".format(letter, next_letter_position))
                    found_letters_positions.append(next_letter_position)
                else:
                    print("word partially found")
                    return False
            return True
        else:
            print("first not found")
            return False

    @staticmethod
    def search_around(self, board, search_from: [int], letter):
        print("search_from: {}".format(search_from))
        print("looking for: {}".format(letter))
        row = search_from[0]
        col = search_from[1]
        print("right")
        position = MySolution.get_middle_right(board, row, col)  # position to search around
        print(position)
        if position is None or board[position[0]][position[1]] != letter:
            print("bottom")
            position = MySolution.get_bottom(board, row, col)
            print(position)
        if position is None or board[position[0]][position[1]] != letter:
            print("left")
            position = MySolution.get_middle_left(board, row, col)
            print(position)
        if position is None or board[position[0]][position[1]] != letter:
            print("top")
            position = MySolution.get_top(board, row, col)
            print(position)
        if position is None or board[position[0]][position[1]] != letter:
            position = None
        return position

    @staticmethod
    def get_top(board, x, y):
        return MySolution.get_position(board, x - 1, y)

    @staticmethod
    def get_middle_left(board, x, y):
        return MySolution.get_position(board, x, y - 1)

    @staticmethod
    def get_middle_right(board, x, y):
        return MySolution.get_position(board, x, y + 1)

    @staticmethod
    def get_bottom(board, x, y):
        return MySolution.get_position(board, x + 1, y)

    @staticmethod
    def get_position(board, x, y):
        try:
            if board[x][y] is not None:
                return [x, y]
            else:
                return None
        except IndexError:
            pass

    @staticmethod
    def find_letter(board, letter):
        print(board)
        for rIdx, row in enumerate(board):
            for cIdx, col in enumerate(row):
                if col == letter:
                    return [rIdx, cIdx]
        return None
