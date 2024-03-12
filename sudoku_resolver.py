sudoku = [
	[9,  [], 7,  [], 8,  2,  3,  [], []],
	[[], 1,  [], [], [], 5,  [] ,[] ,[]],
	[[], [], [], 6,  7,  [], 5,  [], []],
	[[], 6,  [], [], [], [], 2,  [], 3],
	[[], [], 2,  [], 3,  [], 7,  [], 1],
	[[], [], 8,  1,  [], [], [], [], []],
	[[], [], [], 9,  [], [], 4,  [], []],
	[6,  8,  [], [], [], [], [], [], []],
	[3,  9,  [], 7,  [], [], [], [], 8],
]

def fillLists(sudoku):
	for i in range(9):
		for j in range(9):
			if isinstance(sudoku[i][j], list):
				for k in range(1, 10):
					sudoku[i][j].append(k)

def update_line(indLine, sudoku):
	for i in range(9):
		if isinstance(sudoku[indLine][i], int):
			for j in range(9):
				if isinstance(sudoku[indLine][j], list) and sudoku[indLine][i] in sudoku[indLine][j]:
					sudoku[indLine][j].remove(sudoku[indLine][i])
		elif isinstance(sudoku[indLine][i], list) and len(sudoku[indLine][i]) == 1:
			sudoku[indLine][i] = sudoku[indLine][i][0]

def update_column(indColumn, sudoku):
	for i in range(9):
		if isinstance(sudoku[i][indColumn], int):
			for j in range(9):
				if isinstance(sudoku[j][indColumn], list) and sudoku[i][indColumn] in sudoku[j][indColumn]:
					sudoku[j][indColumn].remove(sudoku[i][indColumn])
		elif isinstance(sudoku[i][indColumn], list) and len(sudoku[i][indColumn]) == 1:
			sudoku[i][indColumn] = sudoku[i][indColumn][0]


fillLists(sudoku)
for i in range(50):
	for j in range(9):
		update_line(j, sudoku)
	for k in range(9):
		update_column(k, sudoku)
print(sudoku)


