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
	if sudoku[y].count(number) >= 2:
		return True
	if [n[x] for n in sudoku].count(number) >= 2:
		return True
	square = sudoku[(y // 3) * 3][(x // 3) * 3:(x // 3) * 3 + 3] \
		+ sudoku[(y // 3) * 3 + 1][(x // 3) * 3:(x // 3) * 3 + 3] \
		+ sudoku[(y // 3) * 3 + 2][(x // 3) * 3:(x // 3) * 3 + 3]
	if square.count(number) >= 2:
		return True
	return False

def findXYOfFirst0(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				return j, i
	return -1, -1
def goBackToLastChange(sudoku, indsList):
	i = -1
	x, y = indsList[i]
	while (sudoku[y][x] == 9):
		i -= 1
		if (sudoku[y][x] == 9):
			sudoku[y][x] = 0
		x, y = indsList[i]
print(findXYOfFirst0(sudoku))
sudoku[0][1] = 5
print(isError(sudoku, 1, 0))



