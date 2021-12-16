input_file = open("input", "r")
line = input_file.readline().strip()

def	is_closing(chr):
	if chr == ')' or chr == ']' or chr == '}' or chr == '>':
		return True
	else:
		return False

def	is_opening(chr):
	if chr == '(' or chr == '[' or chr == '{' or chr == '<':
		return True
	else:
		return False

def	get_opener(chr):
	if chr == ')':
		return '('
	if chr == ']':
		return '['
	if chr == '}':
		return '{'
	if chr == '>':
		return '<'

def	get_closer(chr):
	if chr == '(':
		return ')'
	if chr == '[':
		return ']'
	if chr == '{':
		return '}'
	if chr == '<':
		return '>'

def	value_of(chr):
	if chr == ')':
		return 1
	if chr == ']':
		return 2
	if chr == '}':
		return 3
	if chr == '>':
		return 4

scores = []
while line:
	score = 0
	corruption = False
	openings = []
	for ch in line:
		if openings and is_closing(ch):
			if openings[-1] == get_opener(ch):
				openings.pop()
			else:
				corruption = True
				break
		if is_opening(ch):
			openings.append(ch)
	if not corruption:
		for ch in reversed(openings):
			score *= 5
			score += value_of(get_closer(ch))
	if score > 0:
		scores.append(score)
	line = input_file.readline().strip()
scores.sort()
print("Missing Characters Score:", scores[int(len(scores) / 2)])
input_file.close()
