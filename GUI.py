from Globals import *

import pygame
import sys
pygame.init()

RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WHITE = (255,255,255)
GREY = (40,40,30)
BLACK = (0,0,0)

SQUARE_HEIGHT = 20 
SQUARE_WIDTH = 20
DISPLAY_HEIGHT = SQUARE_HEIGHT * SQUARES_VERTICAL
DISPLAY_WIDTH = SQUARE_WIDTH * SQUARES_HORIZONTAL

BACKGROUND_COLOR = WHITE
ACTIVE_PIECE_COLOR = RED
PASSIVE_PIECE_COLOR = BLACK 
LINE_COLOR = RED

window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

class GUI:

	'''
	Board is a 2d array with dimensions SQUARES_HORIZONTAL by
	SQUARES_VERTICAL. It is indexed array[row][col].
	A 0 means no piece present, 1 = piece present.
	array[0][0] corresponds to the top left corner.

	activePieceSquares is an iterable that yields a
	(row, col) tuple or list for each of its four active squares.
	'''

	@staticmethod
	def draw(board, activePieceSquares):

		GUI.checkForQuit()

		window.fill(BACKGROUND_COLOR)

		'''Draw the line above which you can't place
		pieces without losing'''
		leftx = 0
		rightx = DISPLAY_WIDTH
		y = ROW_LOSS*SQUARE_HEIGHT
		pygame.draw.line(window, LINE_COLOR, (leftx, y), (rightx,y))

		for row in range(SQUARES_VERTICAL):
			for col in range(SQUARES_HORIZONTAL):
				if board[row][col]==1: #square present, draw
					GUI.drawRectangle(row, col, PASSIVE_PIECE_COLOR)

		for row, col in activePieceSquares:
			GUI.drawRectangle(row, col, ACTIVE_PIECE_COLOR)

		pygame.display.flip()

	@staticmethod
	def checkForQuit():
		'''This code lets you quit the screen.... but more importantly,
	    looping through the events prevents the screen from freezing.
	    Otherwise the OS sends the screen events which it doesn't respond to,
	    so the OS thinks it is unresponsive and tries to freeze it.'''
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				sys.exit(1)

	@staticmethod
	def drawRectangle(row, col, color):
		xCoord = col*SQUARE_WIDTH
		yCoord = row*SQUARE_HEIGHT
		pygame.draw.rect(window, color, (xCoord, yCoord, SQUARE_WIDTH, SQUARE_HEIGHT))

	@staticmethod
	def getMove():
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit(1)
			if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_LEFT: #pressed left, move left
			        return Moves.LEFT
			    if event.key == pygame.K_RIGHT: #pressed right, move right
			        return Moves.RIGHT
			    if event.key == pygame.K_UP: #pressed up, so rotate the block
			        return Moves.UP
			    if event.key == pygame.K_DOWN:
			    	return Moves.DOWN 










