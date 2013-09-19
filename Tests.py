from GUI import GUI
from Globals import *
from time import sleep
import ActivePiece

boardState = [[0]*SQUARES_HORIZONTAL for i in range(SQUARES_VERTICAL)]
boardState[0][0]=1
# activeSquares = [(0,2)]

for i in range(7):
	activePiece = ActivePiece.NUMBER_PIECE_SUBCLASS[i]()
	for i in range(5):
		activePiece.moveDown()
		GUI.draw(boardState, activePiece.getCoords())
		sleep(.1)
	for i in range(activePiece.numRotations):
		activePiece.rotate()
		GUI.draw(boardState, activePiece.getCoords())
		sleep(.5)

	for i in range(activePiece.numRotations):
		activePiece.rotateBack()
		GUI.draw(boardState, activePiece.getCoords())
		sleep(.5)


sleep(1)



