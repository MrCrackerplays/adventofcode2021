input_file = open("input", "r")
line = input_file.readline().strip()

def	get_risk_if_lowest(x, y, map):
	if y > 0 and (map[y - 1][x] <= map[y][x]):
		return 0
	if x > 0 and (map[y][x - 1] <= map[y][x]):
		return 0
	if y < (len(map) - 1) and (map[y + 1][x] <= map[y][x]):
		return 0
	if x < (len(map[y]) - 1) and (map[y][x + 1] <= map[y][x]):
		return 0
	return int(map[y][x]) + 1

map = []
while line:
	map.append(line)
	line = input_file.readline().strip()

risk = 0
y = 0
while y < len(map):
	x = 0
	while x < len(map[y]):
		risk += get_risk_if_lowest(x, y, map)
		x += 1
	y += 1
print("Risk total:", risk)
input_file.close()
