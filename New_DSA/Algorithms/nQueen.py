class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check for the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if self.board[i][j] == 1:
                return False
        
        return True

    def solve(self, row):
        if row == self.N:
            self.solutions.append([row[:] for row in self.board])
            return True

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(row + 1):
                    return True
                self.board[row][col] = 0

        return False

    def find_first_solution(self):
        if self.solve(0):
            return self.solutions[0]
        else:
            return []

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()

# Example usage:sN
if __name__ == "__main__":
    n = 4  # Size of the chessboard
    queens = NQueens(n)
    first_solution = queens.find_first_solution()
    if first_solution:
        print("First solution found:")
        print_board(first_solution)
    else:
        print("No solution found for", n, "queens.")


