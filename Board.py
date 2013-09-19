from Globals import *
import ActivePiece 
class Board:
	def __init__(self):
		self.piece = ActivePiece.new()
		self.rowsCleared = 0
		self.grid = [[0]*SQUARES_HORIZONTAL for i in range(SQUARES_VERTICAL)]
		self.hasLost = False

	'''returns true if there is a conflict, ie either the piece is out of
	    bounds or the piece overlaps with existing squares'''
	def isConflict(self):
		for row, col in self.piece.getCoords():
			if (not self.inBounds( row, col )) or (row>=0 and self.grid[row][col] ==1):
				print "isConflict is true"
				return True #either of bounds, or hit an overlapping square
		print "isconflict is false"
		return False #each square cleared, so the fxn clears

	def inBounds(self, row, col): #true if in bounds. No restriction for being off the top of the grid, because pieces start partially past the top.
	    return row < SQUARES_VERTICAL and col>=0 and col < SQUARES_HORIZONTAL

	def move(self, move):
		if move==Moves.UP:
			self.rotatePiece()
		elif move==Moves.LEFT:
			self.movePieceLeft()
		elif move==Moves.RIGHT:
			self.movePieceRight()
		elif move==Moves.DOWN:
			self.movePieceDown()

	def movePieceLeft(self): ##Move the piece left if available. Else, don't move the piece.
	    self.piece.moveLeft()
	    if self.isConflict(): ##undo, can't move there
	        self.piece.moveRight()

	def movePieceRight(self): ##move the active piece right if space is available. 
	    self.piece.moveRight()
	    if self.isConflict(): ##undo, can't move there
	        self.piece.moveLeft()

	def movePieceDown(self): ##Move down if space is available. If no space, then add this piece to the static grid & get a new active piece
	    self.piece.moveDown()
	    if self.isConflict(): ##undo, can't move there
	        self.piece.moveUp()
	        self.hitBottom()

	def rotatePiece(self): ##rotate the current piece if space
	    self.piece.rotate()
	    if self.isConflict(): ##undo, can't rotate
	        self.piece.rotateBack() 

	def hitBottom(self):
		for row, col in self.piece.getCoords(): ##add each square to the board
			if row<ROW_LOSS: ##you're past the top of the board when you hit the bottom; you've filled up the board and lose.
			    self.hasLost = True
			self.grid[row][col] = 1
		self.checkFill() #clear out any filled rows
		self.piece = ActivePiece.new() 

	def checkFill(self):
		for row in range(SQUARES_VERTICAL):
			if sum(self.grid[row])==SQUARES_HORIZONTAL:
				del self.grid[row]
				self.grid.insert(0, [0]*SQUARES_HORIZONTAL)

	

