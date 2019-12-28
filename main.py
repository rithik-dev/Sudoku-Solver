class Sudoku:
    def __init__(self, board):
        self.SIZE = 9  # 9x9 board
        self.board = board

    def count_zeroes(self):
        zeroes = 0
        for row in self.board:
            for col in row:
                if col == 0:
                    zeroes += 1
        return zeroes

    @staticmethod
    def get_block(row, col):
        return (row // 3) * 3 + (col // 3) + 1

    @staticmethod
    def transpose(board):
        return list(zip(*board))

    def get_missing_numbers(self, row):
        nums = []
        for i in range(1, self.SIZE + 1):
            if i not in row:
                nums.append(i)
        return nums

    def get_missing_numbers_block(self, block):
        missing = []
        temp = []
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                elem_block = self.get_block(row, col)
                if elem_block == block and self.board[row][col] != 0:
                    temp.append(self.board[row][col])

        for i in range(1, self.SIZE + 1):
            if i not in temp:
                missing.append(i)
        return missing

    def print_board(self):
        board = [x[:] for x in self.board]

        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if board[row][col] == 0:
                    board[row][col] = "_"
                else:
                    board[row][col] = str(board[row][col])

        for i in range(self.SIZE):
            for j in range(0, 12 + 1, 4):
                board[i].insert(j, "|")
            board[i] = " ".join(board[i])

        for j in range(0, 12 + 1, 4):
            board.insert(j, "+-------+-------+-------+")

        board = "\n".join(board)

        print(board)

    def solve(self):
        solve_list = []  # list containing elements to check whether it can solve given board or not
        solved = False
        zeroes = self.count_zeroes()

        while not solved:
            for row in range(self.SIZE):
                for col in range(self.SIZE):
                    solve_list = []
                    if self.board[row][col] == 0:
                        # find missing numbers in row
                        missing_num_row = self.get_missing_numbers(self.board[row])

                        # find missing numbers in column
                        transpose_board = self.transpose(self.board)
                        missing_num_col = self.get_missing_numbers(transpose_board[col])

                        # find missing numbers in block
                        block = self.get_block(row, col)
                        missing_num_block = self.get_missing_numbers_block(block)

                        missing_num_row = set(missing_num_row)
                        missing_num_col = set(missing_num_col)
                        missing_num_block = set(missing_num_block)

                        common = list(missing_num_row & missing_num_col & missing_num_block)

                        if len(common) == 1:
                            self.board[row][col] = common[0]
                            zeroes -= 1

                            if zeroes == 0:
                                solved = True
                                print("SOLVED BOARD")
                                s.print_board()
                        else:
                            solve_list.append(False)

            if not all(solve_list):
                print("Cannot Solve :(")
                break

    def generate_board(self):
        # generate random board here
        pass


BOARD = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

s = Sudoku(BOARD)
print("ORIGINAL BOARD")
s.print_board()
s.solve()

# HARD PUZZLE .. CANNOT SOLVE :(

# BOARD = [
#     [0, 0, 1, 0, 6, 0, 9, 0, 0],
#     [0, 4, 0, 0, 0, 0, 0, 5, 0],
#     [8, 0, 0, 0, 5, 9, 0, 0, 3],
#     [0, 0, 0, 0, 0, 0, 8, 0, 0],
#     [0, 0, 0, 0, 3, 0, 7, 0, 0],
#     [7, 0, 0, 0, 0, 0, 0, 0, 6],
#     [9, 6, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 2, 0],
#     [3, 0, 0, 2, 0, 8, 5, 0, 0]
# ]

# HARDEST SUDOKU  ..cannot solve :(

# BOARD = [
#     [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 6, 0, 0, 0, 0, 0],
#     [0, 7, 0, 0, 9, 0, 2, 0, 0],
#     [0, 5, 0, 0, 0, 7, 0, 0, 0],
#     [0, 0, 0, 0, 4, 5, 7, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 3, 0],
#     [0, 0, 1, 0, 0, 0, 0, 6, 8],
#     [0, 0, 8, 5, 0, 0, 0, 1, 0],
#     [0, 9, 0, 0, 0, 0, 4, 0, 0]
# ]
