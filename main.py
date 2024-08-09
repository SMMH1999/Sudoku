# print("hello this is sudoku game in python !!")

import view
import model
import os

os.system("cls")

sudoku = model.Sudoku()

view.show(sudoku.show())

