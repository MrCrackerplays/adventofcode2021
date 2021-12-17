input_file = open("input", "r")
line = input_file.readline().strip()

def	increase(grid, x, y):
	if len(grid) > 0 and len(grid[0]) > 0 and y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]):
		if grid[y][x] >= 0:
			grid[y][x] += 1
		if grid[y][x] == 10:
			grid[y][x] = -1
			value = 1
			value += increase(grid, x - 1, y - 1)
			value += increase(grid, x, y - 1)
			value += increase(grid, x + 1, y - 1)
			value += increase(grid, x - 1, y)
			value += increase(grid, x + 1, y)
			value += increase(grid, x - 1, y + 1)
			value += increase(grid, x, y + 1)
			value += increase(grid, x + 1, y + 1)
			return (value)
	return (0)

grid = []
while line:
	grid.append(list(map(int, list(line))))
	line = input_file.readline().strip()

flashes = 0
width = len(grid)
height = len(grid[0])
for i in range(100):
	for y in range(width):
		for x in range(height):
			flashes += increase(grid, x, y)
	for y in range(width):
		for x in range(height):
			if grid[y][x] < 0:
				grid[y][x] = 0

print("Total flashes counted", flashes)
input_file.close()
