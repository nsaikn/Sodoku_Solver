# Sudoku Solver
# Saikrishna Chalasani
# Start Date: Feb 23rd, 2017
# End Date: 

import numpy

sudoku = numpy.zeros((9,9))



# inputing initial data
for y in range (0,9):
	print("Enter the sodoku sequence (sapces represent empty boxes) of row {}:".format(y+1))
	row =input('')
	row =list(row)
	for x in range (0,9):
		sudoku[y][x] = row[x]

# display grid 
for y in range (0,9):
	if (y%3) == 0 and y != 0:
		print("--- --- ---")
	for x in range (0,9):
		if x % 3 == 0 and x != 0:
			print('|', end='')
		print(int(sudoku[y][x]), end='')
	print("")

