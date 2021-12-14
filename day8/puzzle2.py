from dataclasses import dataclass

@dataclass
class	SevenSegment:
	top: str = "z"
	bot: str = "z"
	mid: str = "z"
	l_t: str = "z"
	l_b: str = "z"
	r_t: str = "z"
	r_b: str = "z"

@dataclass
class	Numbers:
	one: str = "z"
	two: str = "z"
	three: str = "z"
	four: str = "z"
	five: str = "z"
	six: str = "z"
	seven: str = "z"
	eight: str = "z"
	nine: str = "z"
	zero: str = "z"

def contains_all(string, set):
    for c in set:
        if c not in string: return 0
    return 1

def contains_any(string, set):
    for c in set:
        if c in string: return 1
    return 0

def	exclude_all(string, set):
	for ch in set:
		string = "".join(filter(lambda char: char != ch, string))
	return string

def	segment_to_numb(config, strong):
	if len(strong) == 2:
		return (1)
	elif len(strong) == 4:
		return (4)
	elif len(strong) == 3:
		return (7)
	elif len(strong) == 7:
		return (8)
	elif contains_all(config.two, strong) and contains_all(strong, config.two):
		return (2)
	elif contains_all(config.three, strong) and contains_all(strong, config.three):
		return (3)
	elif contains_all(config.five, strong) and contains_all(strong, config.five):
		return (5)
	elif contains_all(config.six, strong) and contains_all(strong, config.six):
		return (6)
	elif contains_all(config.nine, strong) and contains_all(strong, config.nine):
		return (9)
	elif contains_all(config.zero, strong) and contains_all(strong, config.zero):
		return (0)
	else:
		print("ERROR: STRONG=", strong, "CONFIGURATION=", config)
		return (-1)

def	setup_segment(segment, input):
	one = ""
	four = ""
	seven = ""
	eight = ""
	ftt = []
	nso = []
	for word in input.split(" "):
		if len(word) == 2:
			one = word
		elif len(word) == 4:
			four = word
		elif len(word) == 3:
			seven = word
		elif len(word) == 7:
			eight = word
		elif len(word) == 5:
			ftt.append(word)
		elif len(word) == 6:
			nso.append(word)
	segment.top = exclude_all(seven, one)
	tmb = ""
	three = ""
	five = ""
	two = ""
	for val in ftt:
		if contains_all(val, one):
			#is three
			tmb = exclude_all(val, one)
			three = val
		elif contains_all(val, exclude_all(four, one)):
			#is five
			five = val
		else:
			#is two
			two = val
	mb = [x for x in tmb if x != segment.top]
	for val in mb:
		if contains_any(four, val):
			segment.mid = val
		else:
			segment.bot = val
	segment.l_t = exclude_all(five, three)
	segment.l_b = exclude_all(two, three)
	segment.r_t = exclude_all(one, five)
	segment.r_b = exclude_all(one, two)

def setup_numbers(segment):
	number_config = Numbers()
	number_config.one = segment.r_t + segment.r_b
	number_config.two = segment.top + segment.r_t + segment.mid + segment.l_b + segment.bot
	number_config.three = segment.top + segment.r_t + segment.mid + segment.r_b + segment.bot
	number_config.four = segment.r_t + segment.mid + segment.r_b + segment.l_t
	number_config.five = segment.top + segment.l_t + segment.mid + segment.r_b + segment.bot
	number_config.six = segment.top + segment.l_t + segment.mid + segment.l_b + segment.r_b + segment.bot
	number_config.seven = segment.top + segment.r_t + segment.r_b
	number_config.eight = segment.top + segment.l_t + segment.l_b + segment.r_t + segment.r_b + segment.bot + segment.mid
	number_config.nine = segment.top + segment.l_t + segment.mid + segment.r_t + segment.r_b + segment.bot
	number_config.zero = segment.top + segment.l_t + segment.l_b + segment.r_t + segment.r_b + segment.bot
	return number_config

input_file = open("input", "r")
line = input_file.readline().strip()
total = 0
while line:
	input = line.split("|")[0].strip()
	output = line.split("|")[1].strip()
	segment = SevenSegment()
	setup_segment(segment, input)
	number_config = setup_numbers(segment)
	local = 0
	error = 0
	for	str in output.split(" "):
		local *= 10
		additive = segment_to_numb(number_config, str)
		if additive < 0:
			print("something went massively wrong")
			error = 1
			break
		local += additive
	if error != 0:
		break
	total += local
	line = input_file.readline().strip()
print("total:", total)
input_file.close()
