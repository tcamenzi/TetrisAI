from Globals import *

def playGame(Agent, GUI, GameBoard):
	while(True):
		move = Agent.getMove()
		GameBoard.move(move)
		GUI.draw(GameBoard.grid, GameBoard.piece.getCoords())
		if GameBoard.hasLost:
			break
	print "you have lost!!!"
	

