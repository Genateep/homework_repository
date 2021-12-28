"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from functools import reduce
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks if in the Tic-Tac-Toe 3x3(or more) board are some winners"""

    def _check_rows(board):
        for row in board:
            if len(set(row)) == 1 and row[0] != "-":
                return row[0]
        return 0

    def _check_columns(board):
        for column in list(zip(*reversed(board))):
            if len(set(column)) == 1 and column[0] != "-":
                return column[0]
        return 0

    def _check_diagonals(board):
        if (
            len(set([board[i][i] for i in range(len(board))])) == 1
            and board[0][0] != "-"
        ):
            return board[0][0]
        if (
            len(
                set(
                    [board[i][len(board) - i - 1] for i in range(len(board))]
                )
            ) == 1
            and board[0][len(board) - 1] != "-"
        ):
            return board[0][len(board) - 1]
        return 0

    def _check_winner(b):
        return _check_diagonals(b) or _check_rows(b) or _check_columns(b)

    if _check_winner(board) == "x":
        return "x wins!"
    elif _check_winner(board) == "o":
        return "o wins!"
    elif "-" not in reduce(lambda x, y: x + y, board):
        return "draw!"
    return "unfinished!"
