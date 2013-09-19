from Globals import *
from Model import getAfterStates, MOVES_ORDER
from FeatureExtraction import *

class ComputerAgent:

	FEATURE_VALUE_FUNCTION = {
		'BURIED_SQUARES':getNumBuried,
		'SURFACE_VARIATION':getSurfaceVariation,
		'AVERAGE_HEIGHT':getAverageHeight,
		'TRENCHES_DEPTHS':getTrenchDepths,
		'UNBURY_DISTANCE':getUnburyDistance
	}

	def __init__(self):
		self.featureWeights = self.getInitialFeatureWeights()
		self.features = set(self.featureWeights.keys())

	def getInitialFeatureWeights(self):
		featureWeights = {}
		featureWeights['BURIED_SQUARES'] = 0
		featureWeights['SURFACE_VARIATION'] = 0
		featureWeights['AVERAGE_HEIGHT'] = 0
		featureWeights['TRENCHES_DEPTHS'] = 0
		featureWeights['UNBURY_DISTANCE'] = 0
		return featureWeights

	def getMoves(self, board):
		bestMoves = None
		bestScore = -999999999
		'''afterState is 
		numRotations, numLeft, numRight, numDown, grid
		'''
		for afterState in getAfterStates(board):
			grid = afterState[4]
			currScore = self.score(grid)
			if currScore > bestScore:
				bestScore = currScore
				bestMoves = afterState[:4]


		if bestMoves==None: #no possible moves
			return None 

		moveSequence = []

		'''Take numRotations, numLeft, numRight, numDown
		and use this to generate a sequence of moves; ie numRotations=3
		yields
		[rotate rotate rotate]
		'''

		for index in range(len(MOVES_ORDER)):
			numMoves = bestMoves[index]
			moveType = MOVES_ORDER[index]
			for move in range(numMoves):
				moveSequence.append(moveType)

		#The above sequence moves the piece into place, 
		#but we need it to actually hit bottom to get added; so down one more time.
		moveSequence.append(Moves.DOWN)
		return moveSequence 

	def score(self, grid):
		featureValues = self.getFeatureValues(grid)

		score = 0
		for feature in self.features:
			weight = self.featureWeights[feature]
			value = featureValues[feature]
			score+=weight*value 

		return score 

	def getFeatureValues(self, grid):
		featureValues = {}
		for feature in self.features:
			valueFxn = ComputerAgent.FEATURE_VALUE_FUNCTION[feature]
			value = valueFxn(grid)
			featureValues[feature] = value
		return featureValues 

	


		


