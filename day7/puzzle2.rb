file = File.open("input")
file_data = file.read
file.close
data = file_data.split(',').map{|item| item.to_i }.sort
len = data.length
median = 0
if len.even?
    median = ((data[len / 2] + data[(len / 2) - 1]) / 2)
else
    median = data[len / 2]
end

def fuel_calc(start, target)
    low = [start, target].min
    high = [start, target].max
    step_cost = 1
    fuel = 0
    while low != high do
        fuel += step_cost
        low += 1
        step_cost += 1
    end
    return fuel
end

i = data.min
maximum = data.max
fuel = 4611686018427387903 #max number value
while i < maximum do
    print "calculating fuel for position ", i, ", max position is ", maximum, "\n"
    ifuel = 0
    for n in data do
        ifuel += fuel_calc(n, i)
    end
    fuel = [fuel, ifuel].min
    i += 1
end
print "total fuel cost:", fuel, "\n"
