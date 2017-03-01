# Sudoku Solver
# Saikrishna Chalasani
# Start Date: Feb 23rd, 2017
# End Date: 

######################### FUNCTIONS #########################################
def Compare(a, b): # a is y position and b is x position 
	rowOptions = []
	columnOptions = []
	boxOptions = []
	#compares column
	for y in range(0,9):
		if not isinstance(sudoku[(y,b)], list): #true if box is not blank
			if sudoku[(y,b)] in sudoku[(a,b)]:
				sudoku[(a,b)].remove(sudoku[(y,b)])
		elif y != a:
			columnOptions += sudoku[(y,b)]
		
	# Compares row
	for x in range(0,9):
		if not isinstance(sudoku[(a,x)], list): #true if box is not blank
			if sudoku[(a,x)] in sudoku[(a,b)]:
				sudoku[(a,b)].remove(sudoku[(a,x)])
		elif x != b:
			rowOptions += sudoku[(a,x)]

	for y in range(int(a/3)*3, int(a/3)*3+3):
		for x in range(int(b/3)*3, int(b/3)*3+3):
			if not isinstance(sudoku[(y,x)], list):
				if sudoku[(y,x)] in sudoku[(a,b)]:
					sudoku[(a,b)].remove(sudoku[(y,x)])
			elif y != a or x != b:
				boxOptions += sudoku[(y,x)]

	if len(sudoku[(a,b)]) == 1:
		sudoku[(a,b)] =  sudoku[(a,b)][0]
		return True
	else:
		# columnOptions = set(columnOptions)
		# rowOptions = set(rowOptions)
		# boxOptions = set(boxOptions)
		for each in sudoku[(a,b)]:
			if not each in columnOptions or not each in rowOptions or not each in boxOptions:
				sudoku[(a,b)] = each
				return True
		return False

def Display():
	# display grid 
	for y in range (0,9):
		if (y%3) == 0 and y != 0:
			print("--- --- ---")
		for x in range (0,9):
			if x % 3 == 0 and x != 0:
				print('|', end='')
			if isinstance(sudoku[(y,x)], list):
				print(' ', end="")
			else:
				print(sudoku[(y,x)], end="")
				
		print("")

############################ MAIN ############################################

sudoku= {}
# inputing initial data
for y in range (0,9):
	print("Enter the sodoku sequence (sapces represent empty boxes) of row {}:".format(y+1))
	row =input('')
	row =list(row)
	for x in range (0,9):
		if row[x] != ' ':
			sudoku[(y,x)] = int(row[x])
		else:
			sudoku[(y,x)] = [1,2,3,4,5,6,7,8,9]



notSolved = True
Display()

while(notSolved):
	notSolved = False
	for y in range(0,9):
		for x in range(0,9):

			if isinstance(sudoku[(y,x)], list):
				if not Compare(y,x):
					notSolved = True
	

Display()	
input()	




