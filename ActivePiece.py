from Globals import *
from random import randint


class ActivePiece:
	def __init__(self):
		self.row = START_ROW
		self.col = START_COL

	'''Standard rotation technique for everthing except squares'''
	def rotate(self): ##to rotate a point left about the center, swap x and y then make x negative
		for coord in self.relativePoints:
		    temp = coord[0]
		    coord[0] = coord[1]
		    coord[1] = temp
		    coord[0] *=-1

	'''To rotate the other way, make col negative not row'''
	def rotateBack(self):
		for coord in self.relativePoints:
		    temp = coord[0]
		    coord[0] = coord[1]
		    coord[1] = temp
		    coord[1] *=-1

	def getCoords(self):
		for point in self.relativePoints:
			yield (point[0]+self.row, point[1]+self.col)

	def move(self, move):
		if move==Move.UP:
			self.moveUp()
		elif move==Move.DOWN:
			self.moveDown()
		elif move==Move.RIGHT:
			self.moveRight()
		elif move==Move.LEFT:
			self.moveLeft()

	def moveDown(self):
		self.row+=1

	def moveUp(self):
		self.row-=1

	def moveLeft(self):
	    self.col-=1

	def moveRight(self):
	    self.col+=1

class Square(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 1 #one orientation only
		self.relativePoints = [
			[0,0],
			[0,-1],
			[-1,0],
			[-1,-1]
		]

	'''Squares don't rotate. Doing this
	avoids having the square jump from
	side to side as it rotates about one
	of the 'center' tiles.'''
	def rotate(self): 
		pass

	def rotateBack(self):
		pass 

class LeftS(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 2
		self.relativePoints = [
			[0,0],
			[0,1],
			[-1,0],
			[-1,-1]
		]

class RightS(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 2
		self.relativePoints = [
			[0,0],
			[0,1],
			[1,0],
			[1,-1]
		]

class LeftL(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 4
		self.relativePoints = [
			[0,1],
			[0,0],
			[0,-1],
			[1,-1]
		]

class RightL(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 4
		self.relativePoints = [
			[0,1],
			[0,0],
			[1,0],
			[1,-1]
		]

class Tri(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 4
		self.relativePoints = [
			[0,-1],
			[0,0],
			[0,1],
			[-1,0]
		]

class Line(ActivePiece):
	def __init__(self):
		ActivePiece.__init__(self)
		self.numRotations = 2
		self.relativePoints = [
			[-1,0],
			[0,0],
			[1,0],
			[2,0]
		]


NUMBER_PIECE_SUBCLASS = {
	0:Square,
	1:LeftS,
	2:RightS,
	3:LeftL,
	4:RightL,
	5:Tri,
	6:Line
}

def new():
	newPieceSubclass = NUMBER_PIECE_SUBCLASS[randint(0,6)] #get the class type
	return newPieceSubclass() #construct the instance and return it


