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
	number = sudoku[y][x]
	line = sudoku[y]
	column = [n[x] for n in sudoku]
	if line.count(number) >= 2:
		return True
	if column.count(number) >= 2:
		return True
	# TODO check if error in square
	return False

sudoku[0][2] = 4
print(isError(sudoku, 2, 0))



