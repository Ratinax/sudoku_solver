import sys
from random import randint
def hide_cursor():
	sys.stdout.write('\033[?25l')
	sys.stdout.flush()
def show_cursor():
	sys.stdout.write('\033[?25h')
	sys.stdout.flush()
hide_cursor()
for k in range(10000):
	for i in range(9):
		if i >= 3 and i % 3 == 0:
			sys.stdout.write('\n')
		for j in range(9):
			if j >= 3 and j % 3 == 0:
				sys.stdout.write(' ')
			sys.stdout.write(str((k) % 9))
			# sys.stdout.write("\n")
		sys.stdout.write("\n")
	for i in range(11):
		sys.stdout.write("\033[F")
for i in range(11):
	sys.stdout.write("\n")

show_cursor()
