import sys
from sudoku2Functions import *

def hide_cursor():
	sys.stdout.write('\033[?25l')
	sys.stdout.flush()
def show_cursor():
	sys.stdout.write('\033[?25h')
	sys.stdout.flush()

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
def goBackToLastChange(sudoku, sudoku2, indsList):
	i = -1
	x, y = indsList[i]
	while (len(indsList) > 0 and sudoku2[y][x][-1] >= len(sudoku2[y][x][0]) - 1):
		sudoku[y][x] = 0
		sudoku2[y][x][-1] = -1
		indsList.pop(-1)
		if -i > len(indsList):
			break
		x, y = indsList[i]

def print_sudoku(sudoku):
	for i in range(9):
		if i >= 3 and i % 3 == 0:
			sys.stdout.write('\n')
		for j in range(9):
			if j >= 3 and j % 3 == 0:
				sys.stdout.write(' ')
			sys.stdout.write(str((sudoku[i][j])))
		sys.stdout.write("\n")
	for i in range(11):
		sys.stdout.write("\033[F")
hide_cursor()
sudoku = [
	[6,0,0,0,0,1,3,0,0],
	[0,9,0,0,0,0,0,0,0],
	[0,0,4,0,0,0,0,0,0],
	[0,4,0,0,0,9,0,0,7],
	[0,0,3,0,7,0,9,1,0],
	[0,0,0,4,0,3,6,0,2],
	[3,0,0,7,0,4,0,5,6],
	[0,0,0,0,0,0,0,0,0],
	[2,6,7,5,0,0,0,0,1],
]
# sudoku = [
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0],
# ]

sudoku2 = sort_sudoku(sudoku)
copy_numbers(sudoku, sudoku2)
assign_indexes(sudoku2)

listInds = [findXYOfFirst0(sudoku)]
steps = 0
while True:
	print_sudoku(sudoku)
	steps += 1
	x, y = listInds[-1]
	
	sudoku[y][x] = sudoku2[y][x][0][sudoku2[y][x][-1]]
	sudoku2[y][x][-1] += 1

	if sudoku2[y][x][-1] >= len(sudoku2[y][x][0]):
		goBackToLastChange(sudoku, sudoku2, listInds)
	if isError(sudoku, x, y):
		pass
	else:
		listInds.append(findXYOfFirst0(sudoku))
		if listInds[-1][-1] == -1:
			break

print_sudoku(sudoku)
for i in range(11):
	sys.stdout.write("\n")
show_cursor()
print('Found in', steps, 'steps')