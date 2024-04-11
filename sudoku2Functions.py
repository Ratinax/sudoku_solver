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

def sort_sudoku(sudoku):
	sudoku2 = [line.copy() for line in sudoku]
	fillLists(sudoku2)
	for i in range(50):
		for j in range(9):
			include_line(j, sudoku2)
		for j in range(9):
			include_column(j, sudoku2)
		for j in range(9):
			include_square(j, sudoku2)
		for j in range(9):
			exclude_line(j, sudoku2)
		for j in range(9):
			exclude_column(j, sudoku2)
		for j in range(9):
			exclude_square(j, sudoku2)
	return sudoku2

def copy_numbers(sudoku, sudoku2):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0 and isinstance(sudoku2[i][j], int):
				sudoku[i][j] = sudoku2[i][j]

def assign_indexes(sudoku):
	for i in range(9):
		for j in range(9):
			if isinstance(sudoku[i][j], list):
				sudoku[i][j] = [sudoku[i][j], -1]
			elif isinstance(sudoku[i][j], int):
				sudoku[i][j] = [[sudoku[i][j]], 0]