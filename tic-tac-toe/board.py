class Board:
    def __init__(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def print_board(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 9)

    def is_draw(self):
        for row in self.grid:
            if " " in row:
                return False
        return True

    def place_move(self, row, col, player):
        self.grid[row][col] = player

    def is_cell_empty(self, row, col):
        return self.grid[row][col] == " "