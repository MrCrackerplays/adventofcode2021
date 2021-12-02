input_file = open("input", "r")
line = input_file.readline().strip()
depth = 0
forwards = 0
aim = 0
while line:
	numb = int(line[-1])
	if line.startswith("forward"):
		forwards += numb
		depth += aim * numb
	elif line.startswith("up"):
		aim -= numb
	elif line.startswith("down"):
		aim += numb
	line = input_file.readline().strip()
print(depth, forwards, depth * forwards)
input_file.close()
