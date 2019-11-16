class Switch:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def __repr__(self):
		return f"({self.p1}, {self.p2})"

class State:
	def __init__(self, text):
		data = text.split(",")
		self.data_string = text
		self.position = []

		while(data):
			self.position.append(data.pop(0))

		self.score = self.heuristic()

	def __repr__(self):
		return f'{", ".join(self.position)} | Score = {self.score}'

	# Action
	def move(self, sw):
		aux = self.position[sw.p1]
		self.position[sw.p1] = self.position[sw.p2]
		self.position[sw.p2] = aux

		for i in range(0,len(self.position)):
			if(self.position[i] == str(i)):
				self.position[i] = "-1"

		self.score = self.heuristic()

	# Action preview
	def calculate(self, sw):
		new_state = State(self.data_string)

		aux = new_state.position[sw.p1]
		new_state.position[sw.p1] = new_state.position[sw.p2]
		new_state.position[sw.p2] = aux

		for i in range(0,len(new_state.position)):
			if(new_state.position[i] == str(i)):
				new_state.position[i] = "-1"

		new_state.score = new_state.heuristic()
		return new_state

	# Score function
	def heuristic(self):
		score = 0

		for element in self.position:
			if(element == "-1"):
				score += 1

		return score

# Generates all possible actions
def generate_switches(stat):
	switches = []

	for i in range(0, len(stat.position)):
		for j in range(i, len(stat.position)):
			if(i == j):
				continue
			else:
				if(stat.position[i] == "-1"):
					break
				elif(stat.position[j] == "-1"):
					continue
				else:
					switches.append(Switch(i,j))

	return switches