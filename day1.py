import numpy as np

import utils

lines = utils.get_input(1)
depths = np.array([int(d) for d in lines])

# PART 1

increases = ((depths-np.roll(depths,1))>0).sum()

print("part1:", increases)


# PART 2

windowed_depths = (depths+np.roll(depths,1)+np.roll(depths,2))[2:]
windowed_increases = ((windowed_depths-np.roll(windowed_depths,1))>0).sum()

print("part2:", windowed_increases)

