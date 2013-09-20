from Globals import *
from time import sleep

SLEEP_TIME = .01

def computerPlayGame(ComputerAgent, GUI, GameBoard):
	done = False
	while(not done):
		moveSequence = ComputerAgent.getMoves(GameBoard)
		if moveSequence == None: #no moves, you've lost
			break
		for move in moveSequence:
			GameBoard.move(move)
			GUI.draw(GameBoard.grid, GameBoard.piece.getCoords())
			sleep(SLEEP_TIME)
			if GameBoard.hasLost:
				done = True
				break

	print "you have lost!!!"
	print "you have cleared ", GameBoard.rowsCleared, "rows!!"