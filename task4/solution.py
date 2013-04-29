import re


indexes = {"A3": 21, "B3": 25, "C3": 29, "A2": 53,
           "B2": 57, "C2": 61, "A1": 85, "B1": 89, "C1": 93}

columns = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]

rows = [["A3", "B3", "C3"], ["A2", "B2", "C2"], ["A1", "B1", "C1"]]

diagonals = [["A3", "B2", "C1"], ["A1", "B2", "C3"]]

first_part = "\n  -------------\n3 |   |   |   |\n  -------------\n"
second_part = "2 |   |   |   |\n  -------------\n1 |   | "
third_part = "  |   |\n  -------------\n    A   B   C  \n"


class TicTacToeBoard:
    def __init__(self):
        self.matrix = first_part + second_part + third_part
        self.status = "Game in progress."
        self.last_played = ""

    def __str__(self):
        return self.matrix

    def __getitem__(self, key):
        return self.matrix[indexes[key]]

    def __setitem__(self, key, sign):
        if re.match("^[ABC][123]$", key) is None:
            raise InvalidKey
        if self.matrix[indexes[key]] != ' ':
            raise InvalidMove
        if re.match("^[XO]$", sign) is None:
            raise InvalidValue
        if self.last_played == sign:
            raise NotYourTurn
        self.matrix = change_string(self.matrix, indexes[key], sign)
        self.last_played = sign
        if self.status == "Game in progress.":
            for keys in [rows, columns, diagonals]:
                if check_keys(self.matrix, keys, sign):
                    self.status = "{} wins!".format(sign)
                    return
            if not ' ' in map(lambda x: self.matrix[indexes[x]],
                              list(indexes.keys())):
                self.status = "Draw!"

    def game_status(self):
        return self.status


def change_string(string, index, new_char):
    list_of_chars = list(string)
    list_of_chars[index] = new_char
    return ''.join(list_of_chars)


def check_keys(matrix, keys, sign):
    for row in keys:
        if len([elem for elem in row if matrix[indexes[elem]] == sign]) == 3:
            return True
    return False


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass
