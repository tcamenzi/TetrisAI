from Globals import *

HEIGHT_NORMALIZATION = 1
SURFACE_VARIATION_NORMALIZATION = 1

'''Feature value is always 1; basically adds in a constant to our linear fxn
so we have a base score approximation, ie for a blank grid.'''
def getBaseValue(grid):
	return 1

	
'''Return the number of 'buried' squares, that is
the number of unfilled squares that have filled 
squares above them.'''
def getNumBuried(grid):
	total = 0
	for col in range(SQUARES_HORIZONTAL):
		for row in range(0, SQUARES_VERTICAL):
			if grid[row][col]==1: #find first filled
				break
			row+=1 #move to next square
		for row in range(row, SQUARES_VERTICAL): #find all filled below here
			if grid[row][col]==0:
				total+=1

	return total 

'''Helper function.
Return the index of the highest filled square 
in the given column, or 
SQUARES_VERTICAL if there is none filled.'''
def getHighestFilled(grid, col):
	for row in range(0, SQUARES_VERTICAL):
		if grid[row][col]==1:
			return row 
	return SQUARES_VERTICAL

def getSurfaceVariation(grid):
	total = 0

	first = getHighestFilled(grid, 0)
	for col in range(SQUARES_HORIZONTAL-1):
		second = getHighestFilled(grid, col+1)
		total+=abs(second-first)**2 #square difference
		first = second 

	return total*SURFACE_VARIATION_NORMALIZATION 

def getAverageHeight(grid):
	total=0
	for rowindex in range(SQUARES_VERTICAL):
		total+=sum(grid[rowindex])*(SQUARES_VERTICAL-rowindex) #10 for top, 9 for next, etc.
	return total*HEIGHT_NORMALIZATION

def getUnburyDistance(grid):
	firstCovered = [SQUARES_VERTICAL]*SQUARES_HORIZONTAL #0 = covered at top; SQUARES_VERTICAL = uncovered
	for rowindex in range(SQUARES_VERTICAL):
		row = grid[rowindex]
		for colindex in range(SQUARES_HORIZONTAL):
			curr = row[colindex]
			if curr==0 and firstCovered[colindex]<rowindex: #covered
				return rowindex - firstCovered[colindex] #distance to unbury
			if curr==1:
				firstCovered[colindex] = min(rowindex, firstCovered[colindex])
	#none covered
	return 0

def getTrenchDepths(grid):
	heights = [SQUARES_VERTICAL] #treat the edge as being very tall
	for col in range(SQUARES_HORIZONTAL):
		height = SQUARES_VERTICAL - getHighestFilled(grid, col)
		heights.append(height)
	heights.append(SQUARES_VERTICAL)

	trenchDepths = 0
	for col in range(1, SQUARES_HORIZONTAL+1):
		left = heights[col-1]
		right = heights[col+1]
		curr = heights[col]
		lowerSide = min(left,right)

		if lowerSide > curr: #it's a trench
			trenchDepths += (lowerSide-curr)**2 #get the difference squared

	return trenchDepths 