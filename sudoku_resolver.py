import sys

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
	while (len(indsList) > 0 and sudoku[y][x] == 9):
		sudoku[y][x] = 0
		i -= 1
		indsList.pop(-1)
		x, y = indsList[i]

def print_sudoku(sudoku):
	for i in range(9):
		if i >= 3 and i % 3 == 0:
			sys.stdout.write('\n')
		for j in range(9):
			if j >= 3 and j % 3 == 0:
				sys.stdout.write(' ')
			sys.stdout.write(str((sudoku[i][j]) % 9))
		sys.stdout.write("\n")
	for i in range(11):
		sys.stdout.write("\033[F")

# print(findXYOfFirst0(sudoku))
# sudoku[0][1] = 5
# print(isError(sudoku, 1, 0))

print_sudoku(sudoku)

for i in range(11):
	sys.stdout.write("\n")
