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
	map.append(list(line))
	line = input_file.readline().strip()

def	flood_fill(y, x, map):
	size = 0
	if map[y][x] != "9" and map[y][x] != "f":
		map[y][x] = "f"
		size += 1
		if 0 < y:
			size += flood_fill(y - 1, x, map)
		if y < (len(map) - 1):
			size += flood_fill(y + 1, x, map)
		if 0 < x:
			size += flood_fill(y, x - 1, map)
		if x < (len(map[y]) - 1):
			size += flood_fill(y, x + 1, map)
	return (size)

def	print_map(map):
	for line in map:
		print(line)

basins = []
y = 0
while y < len(map):
	x = 0
	while x < len(map[y]):
		size = 0
		size = flood_fill(y, x, map)
		if size > 0:
			basins.append(size)
		x += 1
	y += 1
top_basins = sorted(basins, reverse=True)[:3]
result = top_basins[0] * top_basins[1] * top_basins[2]
print("largest basins:", top_basins, "multiplied:", result)
# print("BASIN FILLED MAP")
# print_map(map)
input_file.close()
