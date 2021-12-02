import utils

lines = utils.get_input(2)

# PART 1

depth = 0
horizontal = 0

for line in lines:
	direction, value = line.split(' ')
	value = int(value)

	if direction=='up':
		depth -= value
	if direction=='down':
		depth += value
	if direction=='forward':
		horizontal += value

print("part1:", depth * horizontal)


# PART 2

depth = 0
horizontal = 0
aim = 0

for line in lines:
	direction, value = line.split(' ')
	value = int(value)

	if direction=='up':
		aim -= value
	if direction=='down':
		aim += value
	if direction=='forward':
		horizontal += value
		depth += aim * value

print("part2:", depth * horizontal)
