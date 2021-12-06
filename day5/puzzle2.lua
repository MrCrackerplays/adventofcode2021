-- http://lua-users.org/wiki/FileInputOutput

-- see if the file exists
function file_exists(file)
	local f = io.open(file, "rb")
	if f then f:close() end
	return f ~= nil
end

-- get all lines from a file, returns an empty 
-- list/table if the file does not exist
function lines_from(file)
	if not file_exists(file) then return {} end
	lines = {}
	for line in io.lines(file) do 
		lines[#lines + 1] = line
	end
	return lines
end

local file = 'example'
local lines = lines_from(file)

local danger_positions = {}

function add_position(x, y)
	if not danger_positions[y] then
		danger_positions[y] = {}
	end
	if danger_positions[y][x] then
		danger_positions[y][x] = danger_positions[y][x] + 1
	else
		danger_positions[y][x] = 1
	end
end

function count_danger_positions()
	local count = 0
	for y,values in pairs(danger_positions) do
		for x, amount in pairs(values) do
			if amount > 1 then
				print(x .. " " .. y .. " = " .. amount)
				count = count + 1
			end
		end
	end
	return count
end

function is_diagonal(x1, x2, y1, y2)
	if math.max(x1,x2) - math.min(x1,x2) == math.max(y1,y2) - math.min(y1,y2) then
		return true
	end
	return false
end

function walk_line(x1, y1, x2, y2)
	local diag = is_diagonal(x1, y1, x2, y2)
	if x1 ~= x2 and y1 ~= y2 and not diag then
		return
	end
	if not diag then
		for i=math.min(y1,y2),math.max(y1,y2) do
			for j=math.min(x1,x2),math.max(x1,x2) do
				add_position(j, i)
			end
		end
	else
		for i=0,math.max(y1,y2) - math.min(y1,y2) do
			add_position(math.min(x1,x2) + i, math.min(y1,y2) + i)
		end
	end
end

--for every line extract the numbers and walk the line they make
for k,v in pairs(lines) do
	v = v:gsub(" %-> ", ",")
	i = 0
	positions = {}
	for s in string.gmatch(v, "[^,]+") do
		positions[i] = tonumber(s)
		i = i + 1
	end
	walk_line(positions[0], positions[1], positions[2], positions[3])
end

print("amount of dangerous positions where amount of lines crossed > 1 is:", count_danger_positions())
