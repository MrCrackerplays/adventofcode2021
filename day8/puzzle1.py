input_file = open("input", "r")
line = input_file.readline().strip()

one = 2
four = 4
seven = 3
eight = 7
uniques = 0
while line:
	input = line.split("|")[0]
	output = line.split("|")[1]
	for	str in output.split(" "):
		if len(str) in {one, four, seven, eight}:
			uniques += 1
	line = input_file.readline().strip()
print("uniques:", uniques)
input_file.close()
