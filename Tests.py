from GUI import GUI
from Globals import *
from time import sleep
import ActivePiece
from Board import Board
from HumanAgent import HumanAgent 
from playGame import playGame 
# boardState = [[0]*SQUARES_HORIZONTAL for i in range(SQUARES_VERTICAL)]
# boardState[0][0]=1
# activeSquares = [(0,2)]

# for i in range(7):
# 	activePiece = ActivePiece.NUMBER_PIECE_SUBCLASS[i]()
# 	for i in range(5):
# 		activePiece.moveDown()
# 		GUI.draw(boardState, activePiece.getCoords())
# 		sleep(.1)
# 	for i in range(activePiece.numRotations):
# 		activePiece.rotate()
# 		GUI.draw(boardState, activePiece.getCoords())
# 		sleep(.5)

# 	for i in range(activePiece.numRotations):
# 		activePiece.rotateBack()
# 		GUI.draw(boardState, activePiece.getCoords())
# 		sleep(.5)


# sleep(1)

board = Board()
agent = HumanAgent(GUI)

playGame(agent, GUI, board)
# board.piece.row+=5
# for coord in board.piece.getCoords():
#  	print coord 
# GUI.draw(board.grid, board.piece.getCoords())


# while(True):
# 	temp = raw_input("Enter move here (q to quit)")
# 	if temp=='q':
# 		break
# 	elif temp=='l':
# 		board.move(Moves.LEFT)
# 	elif temp=='r':
# 		board.move(Moves.RIGHT)
# 	elif temp=='u':
# 		board.move(Moves.UP)
# 	elif temp=='d':
# 		board.move(Moves.DOWN)
# 	for coord in board.piece.getCoords():
# 		print coord 
# 	GUI.draw(board.grid, board.piece.getCoords())
	# sleep(1)






