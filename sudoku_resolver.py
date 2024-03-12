sudoku = [
	[3, 0, 0, 0, 1, 0, 4, 0, 0],
	[0, 0, 2, 0, 5, 0, 0 ,0 ,0],
	[8, 0, 0, 4, 0, 2, 0, 6, 0],
	[0, 3, 0, 0, 0, 0, 0, 5, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 9, 8, 0, 4, 3, 0, 0],
	[0, 0, 0, 0, 2, 0, 0, 0, 0],
	[0, 0, 8, 3, 0, 9, 5, 0, 0],
	[6, 0, 0, 0, 0, 0, 0, 0, 7],
]

def isError(sudoku, x, y):
	for i in range(9):
		if i != x: # check if error on x (abscissa)
			if sudoku[y][i] == sudoku[y][x]:
				return True
		if i != y:
			if sudoku[i][x] == sudoku[y][x]: # check if error on y (ordinate)
				return True
	# TODO check if error in square
	return False

sudoku[0][2] = 7
print(isError(sudoku, 2, 0))



