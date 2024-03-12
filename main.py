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
		for j in range(9):
			sys.stdout.write(str((k) % 9))
		sys.stdout.write("\n")

	sys.stdout.write("\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F")
for i in range(9):
	sys.stdout.write("\n")

show_cursor()
