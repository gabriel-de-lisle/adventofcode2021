import numpy as np

if __name__=='__main__':
	with open("inputs/day1.txt", "r") as f:
		data = f.read()

	depths = np.array([int(d) for d in data.split('\n')[:-1]])

	increases = ((depths-np.roll(depths,1))>0).sum()
	print("part1:", increases)

	windowed_depths = (depths+np.roll(depths,1)+np.roll(depths,2))[2:]
	windowed_increases = ((windowed_depths-np.roll(windowed_depths,1))>0).sum()
	print("part2:", windowed_increases)

