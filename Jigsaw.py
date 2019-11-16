from State import *

s = State("3,7,2,1,8,4,5,0,6")
final_state = 9
current_score = 0
path = []
decision = []

while(s.score < final_state):
	for sw in generate_switches(s):
		aux = s.calculate(sw)
		decision.append([aux.heuristic(), sw])

	sorted_decision = sorted(decision, key=lambda element: element[0])
	path.append(sorted_decision[-1][1:])
	s.move(path[-1][0])
	decision = []

print(path)
