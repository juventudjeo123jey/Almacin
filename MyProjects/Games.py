def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            num = board[i][j]
            row += str(num) + " "
            if (j + 1) % 3 == 0 and j < 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)

def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    print("Enter your Sudoku puzzle (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != 9 or not all(0 <= x <= 9 for x in row):
                    raise ValueError
                board.append(row)
                break
            except ValueError:
                print("Invalid input. Enter 9 numbers between 0 and 9 separated by spaces.")

    print("\nSolving Sudoku...\n")
    if solve(board):
        print("Solved Sudoku:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku.")

if __name__ == "__main__":
    main()