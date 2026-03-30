from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def check_win(self, player):
        grid = self.board.grid

        # rows
        for row in grid:
            if row[0] == row[1] == row[2] == player:
                return True

        # columns
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] == player:
                return True

        # diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] == player:
            return True

        if grid[0][2] == grid[1][1] == grid[2][0] == player:
            return True

        return False

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def start(self):
        while True:
            print("current player:", self.current_player)
            self.board.print_board()

            row = int(input("Enter a row(0-2): "))
            col = int(input("Enter a col(0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position")
                continue

            if not self.board.is_cell_empty(row, col):
                print("Position already filled")
                continue

            self.board.place_move(row, col, self.current_player)

            if self.check_win(self.current_player):
                self.board.print_board()
                print(f"{self.current_player} wins!")
                break

            if self.board.is_draw():
                self.board.print_board()
                print("It's a draw!")
                break

            self.switch_player()


game = Game()
game.start()