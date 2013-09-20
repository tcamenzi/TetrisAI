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
		self.numMoves = 10
		self.initialAlpha = 0
		self.alpha = self.initialAlpha/(self.numMoves**.2)
		self.previousFeatureValues = self.getZeroFeatureValues()
		self.previousScore = 0

	def getZeroFeatureValues(self):
		featureValues = {}
		for feature in self.features:
			featureValues[feature] = 0
		return featureValues 

	def getInitialFeatureWeights(self):
		featureWeights = {}
		featureWeights['BURIED_SQUARES'] = -20
		featureWeights['SURFACE_VARIATION'] = -1
		featureWeights['AVERAGE_HEIGHT'] = 0
		featureWeights['TRENCHES_DEPTHS'] = -1
		featureWeights['UNBURY_DISTANCE'] = -1
		return featureWeights

	def getMoves(self, board):

		self.numMoves += 1
		self.alpha = self.initialAlpha/(self.numMoves**.2)

		bestMoves = None
		bestFeatures = None 
		bestScore = None
		'''afterState is 
		numRotations, numLeft, numRight, numDown, grid
		'''
		for afterState in getAfterStates(board):
			grid = afterState[4]
			currScore, currFeatures = self.score(grid)
			if bestScore == None or currScore > bestScore:
				bestScore = currScore
				bestFeatures = currFeatures 
				bestMoves = afterState[:4]

		print "bestScore: ", bestScore 


		if bestMoves==None: #no possible moves, you've lost: end state value is REWARD_ON_LOSS/numRowsCleared (negative)
			episodeReward = REWARD_ON_LOSS / (board.rowsCleared+1)
			error = episodeReward - self.previousScore 
			self.updateFeatureWeights(error)

			print ""
			print "FEATURE WEIGHTS"
			for feature in self.featureWeights:
				print feature, self.featureWeights[feature]

			'''Reset to initial values'''
			self.previousScore = 0
			self.previousFeatureValues = self.getZeroFeatureValues()
			return None 

		#print featues
		if self.numMoves %100==0:
			print ""
			print "FEATURE VALUES:"
			for feature in bestFeatures:
				print feature, bestFeatures[feature]
			print ""
			print "FEATURE WEIGHTS"
			for feature in self.featureWeights:
				print feature, self.featureWeights[feature]

			# print "grid: "
			# print board.grid 

			print "num rows cleared: "
			print board.rowsCleared 
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


		'''Learning goes here'''
		error = bestScore - self.previousScore
		self.updateFeatureWeights(error)
		self.previousScore = bestScore
		self.previousFeatureValues = bestFeatures

		return moveSequence 

	def updateFeatureWeights(self, error):
		coefficient = error*self.alpha
		for feature in self.features:
			gradient = self.previousFeatureValues[feature] #linear case: gradient equals value of that feature
			update = coefficient*gradient 
			self.featureWeights[feature]+=update

		self.normalizeFeatureWeights()

	'''So they don't grow unbounded, normalize 
	back to 1.'''
	def normalizeFeatureWeights(self):
		return 
		total = 0
		for feature in self.features:
			total+=self.featureWeights[feature]**2
		total=(total**.5) #the 2-norm

		if total==0:
			return 

		for feature in self.features:
			self.featureWeights[feature]/=total



	def score(self, grid):
		featureValues = self.getFeatureValues(grid)

		score = 0
		for feature in self.features:
			weight = self.featureWeights[feature]
			value = featureValues[feature]
			score+=weight*value 

		return score, featureValues 

	def getFeatureValues(self, grid):
		featureValues = {}
		for feature in self.features:
			valueFxn = ComputerAgent.FEATURE_VALUE_FUNCTION[feature]
			value = valueFxn(grid)
			featureValues[feature] = value
		return featureValues 

	


		


