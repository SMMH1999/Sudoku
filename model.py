"""model of sudoku game

Returns:
    Sudoku object
"""

import random


class Sudoku:
    """This is Sudoku class

    in this class we use to methods for creating sudoku
    """

    def __init__(self) -> None:
        self.__board = [[" " for _ in range(9)] for _ in range(9)]
        self.__generate()

    def __generate(self):
        """__generate _summary_

        A very powerful method to initialize a Sudoku grid is to use a backtracking algorithm,
        which attempts to fill the grid while backtracking
        whenever it hits a violation of Sudoku rules.
        This method can generate fully solved Sudoku grids.

        Returns:
            bool: It starts recursively initializing the table, if it does not encounter an error,
            it returns the correct value, otherwise it returns the false value.
        """

        numbers = range(1, 10)
        samples = random.sample(numbers, 9)

        for i in range(9):
            for j in range(9):
                if self.__board[i][j] == " ":
                    for num in samples:
                        if self.__is_valid(i, j, num):
                            self.__board[i][j] = num
                            if self.__generate():
                                return True
                            self.__board[i][j] = 0
                    return False
        return True

    def __is_valid(self, row, col, value):
        """__is_valid The check was valid for a value in a specified location

        it is checked whether the entered value is suitable for the selected location,
        which is in terms of rows and columns.
        For each row, column and 3*3 area of the table, according to Sudoku rules,
        the values are checked to confirm the validity of the values.

        Args:
            row (int): The desired row
            col (int): The desired column
            value (int): The value to be checked

        Returns:
            bool: It indicates the validity or not of the number entered for the desired position
        """
        for i in range(9):
            if self.__board[row][i] == value or self.__board[i][col] == value:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)

        for i in range(3):
            for j in range(3):
                if self.__board[i + start_row][j + start_col] == value:
                    return False
        return True

    def show(self) -> list[list]:
        """show show board

        Return the Sudoku Board
        """
        return self.__board

    def regenerate(self):
        """regenerate regenerate sudoku

        regenerating the sudoku with Backtracking method
        """
        self.__generate()
