input_file = open("input", "r")
line = input_file.readline().strip()
depth = 0
forwards = 0
while line:
	if line.startswith("forward"):
		forwards += int(line[-1])
	elif line.startswith("up"):
		depth -= int(line[-1])
	elif line.startswith("down"):
		depth += int(line[-1])
	line = input_file.readline().strip()
print(depth, forwards, depth * forwards)
input_file.close()
