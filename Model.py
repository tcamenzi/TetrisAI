from Globals import *
from copy import deepcopy
'''This is a generator function that,
given a board state and active piece, will return the
board states for all possible endings of the active piece.
The next effect of this generator will be read-only; that is,
the board & active piece will be the same at the end of the 
funtion as they are at the start.
However, for efficiency, at intermediate states they may differ
from the original board.
For each state, we yield both the end state and the moves (number 
of rotations, left/right moves, and down moves) required to reach
that end state.

Note that the state will only be the same *after* all iterations
of the generator have completed. Before all iterations have completed--
or if iteration is interrupted-- then the state may be changed.

Output is a tuple
(numRotations, numLeft, numRight, numDown, board)
'''

#Specify the order in which moves are returned, ie
#numRotations, numLeft, numRight, numDown
MOVES_ORDER	= (Moves.UP, Moves.LEFT, Moves.RIGHT, Moves.DOWN)

def getAfterStates(board):
	origBoard = deepcopy(board) #for testing only

	activePiece = board.piece 
	for numRotations in range(activePiece.numRotations):
		for item in getAllWithinRotation(board, activePiece):
			yield (numRotations,)+item 
		activePiece.rotate()

	for numRotations in range(activePiece.numRotations):
		activePiece.rotateBack()

	#check it's the same, for testing only
	assert(origBoard.grid==board.grid)
	oap = origBoard.piece
	bap = board.piece
	assert(oap.relativePoints==bap.relativePoints)
	assert(oap.row==bap.row)
	assert(oap.col==bap.col)

def getAllWithinRotation(board, activePiece):

	'''Get all to the left'''
	movesLeft = 0
	while(not board.isConflict()):
		for item in getMoveDown(board, activePiece):
			yield (movesLeft, 0)+item 
		movesLeft+=1
		activePiece.moveLeft()

	for i in range(movesLeft):
		activePiece.moveRight()

	'''Get all to the right'''
	activePiece.moveRight()
	movesRight = 1
	while(not board.isConflict()):
		for item in getMoveDown(board, activePiece):
			yield (0, movesRight)+item 
		movesRight+=1
		activePiece.moveRight()

	for i in range(movesRight):
		activePiece.moveLeft()

def getMoveDown(board, activePiece):
	movesDown = 0
	while(not board.isConflict()):
		activePiece.moveDown()
		movesDown+=1

	#There's been a conflict, go up 1 to no conflict
	movesDown-=1
	activePiece.moveUp()

	'''If you're above the top of the board, this move is illegal,
	don't even consider it.'''
	for row, col in activePiece.getCoords():
		if row<ROW_LOSS: #illegal
			'''We want to return without yielding, but first
			we have to move the piece up to its original position.'''
			for i in range(movesDown):
				activePiece.moveUp()
			return

	'''Add to board'''
	for row, col in activePiece.getCoords():
		board.grid[row][col]=1

	'''Check for filled rows'''
	filledRowIndexes = []
	for rowindex in range(SQUARES_VERTICAL):
		if sum(board.grid[rowindex])==SQUARES_HORIZONTAL:
			filledRowIndexes.append(rowindex)

	'''Remove filled rows'''
	for filledIndex in filledRowIndexes:
		del board.grid[filledIndex]
		board.grid.insert(0, [0]*SQUARES_HORIZONTAL)


	yield (movesDown, board.grid)

	'''Add back in filled rows'''
	for filledIndex in filledRowIndexes[::-1]:
		del board.grid[0]
		board.grid.insert(filledIndex, [1]*SQUARES_HORIZONTAL)

	'''remove from board'''
	for row, col in activePiece.getCoords():
		board.grid[row][col]=0

	for i in range(movesDown):
		activePiece.moveUp()











