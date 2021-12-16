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
		return 3
	if chr == ']':
		return 57
	if chr == '}':
		return 1197
	if chr == '>':
		return 25137

j = 0
points = 0
while line:
	openings = []
	i = 0
	for ch in line:
		if openings and is_closing(ch):
			if openings[-1] == get_opener(ch):
				openings.pop()
			else:
				# print("Corruption at", j, ":", i, "expected", get_closer(openings[-1]), "but found", ch, "instead")
				points += value_of(ch)
				break
		if is_opening(ch):
			openings.append(ch)
		i += 1
	line = input_file.readline().strip()
	j += 1
print("Syntax Error Score:", points)
input_file.close()
