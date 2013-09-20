SQUARES_VERTICAL = 28
SQUARES_HORIZONTAL = 10
START_ROW = 0 #pieces start at the top of the board
START_COL = SQUARES_HORIZONTAL / 2

ROW_LOSS = 3 #anything above 0 is losing
REWARD_ON_LOSS = -100

class Moves:
	UP = 0
	LEFT = 1
	RIGHT = 2
	DOWN = 3
