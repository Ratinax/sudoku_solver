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

def fillLists(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				sudoku[i][j] = []
				for k in range(1, 10):
					sudoku[i][j].append(k)

def include_line(indLine, sudoku):
	for i in range(9):
		if isinstance(sudoku[indLine][i], int):
			for j in range(9):
				if isinstance(sudoku[indLine][j], list) and sudoku[indLine][i] in sudoku[indLine][j]:
					sudoku[indLine][j].remove(sudoku[indLine][i])
		elif isinstance(sudoku[indLine][i], list) and len(sudoku[indLine][i]) == 1:
			sudoku[indLine][i] = sudoku[indLine][i][0]

def include_column(indColumn, sudoku):
	for i in range(9):
		if isinstance(sudoku[i][indColumn], int):
			for j in range(9):
				if isinstance(sudoku[j][indColumn], list) and sudoku[i][indColumn] in sudoku[j][indColumn]:
					sudoku[j][indColumn].remove(sudoku[i][indColumn])
		elif isinstance(sudoku[i][indColumn], list) and len(sudoku[i][indColumn]) == 1:
			sudoku[i][indColumn] = sudoku[i][indColumn][0]

def include_square(indSquare, sudoku):
	x = (indSquare % 3) * 3
	y = (indSquare // 3) * 3
	for i in range(3):
		for j in range(3):
			if isinstance(sudoku[y + i][x + j], int):
				for i2 in range(3):
					for j2 in range(3):
						if isinstance(sudoku[y + i2][x + j2], list) and sudoku[y + i][x + j] in sudoku[y + i2][x + j2]:
							sudoku[y + i2][x + j2].remove(sudoku[y + i][x + j])
			elif isinstance(sudoku[y + i][x + j], list) and len(sudoku[y + i][x + j]) == 1:
				sudoku[y + i][x + j] = sudoku[y + i][x + j][0]

def exclude_line(indLine, sudoku):
	for i in range(9):
		if isinstance(sudoku[indLine][i], list):
			for j in range(len(sudoku[indLine][i])):
				isSolo = True
				for k in range(9):
					if isinstance(sudoku[indLine][k], list) and sudoku[indLine][i][j] in sudoku[indLine][k]:
						isSolo = False
						break
				if isSolo:
					sudoku[indLine][i] = sudoku[indLine][i][j]

def exclude_column(indColumn, sudoku):
	for i in range(9):
		if isinstance(sudoku[i][indColumn], list):
			for j in range(len(sudoku[i][indColumn])):
				isSolo = True
				for k in range(9):
					if isinstance(sudoku[k][indColumn], list) and sudoku[i][indColumn][j] in sudoku[k][indColumn]:
						isSolo = False
						break
				if isSolo:
					sudoku[i][indColumn] = sudoku[i][indColumn][j]

def exclude_square(indSquare, sudoku):
	x = (indSquare % 3) * 3
	y = (indSquare // 3) * 3
	for i in range(3):
		for j in range(3):
			if isinstance(sudoku[y + i][x + j], list):
				for k in range(len(sudoku[y + i][x + j])):
					isSolo = True
					for i2 in range(3):
						for j2 in range(3):
							if isinstance(sudoku[y + i2][x + j2], list) and sudoku[y + i][x + j][k] in sudoku[y + i2][x + j2]:
								isSolo = False
								break
					if isSolo:
						sudoku[y + i][x + j] = sudoku[y + i][x + j][k]

def addSpaces(str, size):
	# print(len(str))
	spacesNbr = int(int(size - len(str)) / 2)
	res = spacesNbr * ' ' + str + spacesNbr * ' '
	return res

fillLists(sudoku)
# TODO do that while solution not found
for i in range(100): # TODO change value to do while for better solution
	for j in range(9):
		include_line(j, sudoku)
	for j in range(9):
		include_column(j, sudoku)
	for j in range(9):
		include_square(j, sudoku)
	for j in range(9):
		exclude_line(j, sudoku)
	for j in range(9):
		exclude_column(j, sudoku)
	for j in range(9):
		exclude_square(j, sudoku)
# TODO save sudoku state in memory
# TODO take a list and asign it its number
# TODO repeat
# IF error, go back to solution and choose something else


total_bt = 1
for l in sudoku:
	for case in l:
		if isinstance(case, list):
			total_bt += len(case)
		print(addSpaces(str(case), 20), end = "")
	print()

print(total_bt)


