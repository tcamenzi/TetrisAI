# from GUI import GUI
from FakeGui import FakeGui
from Globals import *
from time import sleep
import ActivePiece
from Board import Board
from HumanAgent import HumanAgent 
from ComputerAgent import ComputerAgent 
from humanPlayGame import humanPlayGame 
from computerPlayGame import computerPlayGame 
from Model import getAfterStates
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

# board = Board()
# for i in range(4):
# 	board.piece.moveDown()
# GUI.draw(board.grid, board.piece.getCoords())

# for numRotations, numLeft, numRight, numDown, grid in getAfterStates(board):
# 	print "numRotations: ", numRotations
# 	print "numLeft: ", numLeft
# 	print "numRight: ", numRight
# 	print "numDown: ", numDown
# 	GUI.draw(grid, board.piece.getCoords())
# 	raw_input("enter to continue")

# agent = HumanAgent(GUI)

# playGame(agent, GUI, board)
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

# humanAgent = HumanAgent(GUI)
# humanPlayGame(humanAgent, GUI, board)


computerAgent = ComputerAgent()
for i in range(100):
	board = Board()
	computerPlayGame(computerAgent, FakeGui, board)

# board = Board()
# board.grid = 




