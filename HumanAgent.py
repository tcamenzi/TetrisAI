from Globals import *
class HumanAgent:
	def __init__(self, GUI):
		self.GUI = GUI

	def getMove(self):
		return self.GUI.getMove()