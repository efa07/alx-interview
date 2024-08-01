"""
Use Backtracking algorithm to place N non-attacking
 queens on an N x N chessboard.
"""
import sys

def is_safe(board, row, col):
    """
    Check if a queen can be safely placed at board[row][col].
    
    Args:
        board (list): n by n list representing the chessboard.
        row (int): The row index where the queen is to be placed.
        col (int): The column index where the queen is to be placed.
    
    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col):
    """
    Solve the N queens problem using backtracking.
    
    Args:
        board (list): 2D list representing the chessboard.
        col (int): The current column index to place the queen.
    
    Returns:
        bool: True if the queen can be placed in any row of this column, False otherwise.
    """
    # If all queens are placed, print the solution
    if col >= len(board):
        print_solution(board)
        return True
    
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1
            
            # Recur to place the rest of the queens
            res = solve_nqueens_util(board, col + 1) or res
            
            # Backtrack if placing queen in board[i][col] doesn't lead to a solution
            board[i][col] = 0
    
    return res

def print_solution(board):
    """
    Print the board configuration as a list of [row, col] pairs where queens are placed.
    
    Args:
        board (list): 2D list representing the chessboard.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def solve_nqueens(N):
    """
    Initialize the chessboard and solve the N queens problem.
    
    Args:
        N (int): The size of the chessboard (N×N).
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0)

def main():
    """
    Main function to handle input validation and initiate the solving process.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)

if __name__ == "__main__":
    main()
