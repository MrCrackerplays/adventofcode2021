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
puts "the median of all values (aka the position to go to) is:", median

fuel = 0

for i in data do
    fuel += (median - i).abs()
end
puts "total fuel cost:", fuel
