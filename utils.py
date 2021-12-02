def get_input(i):
	with open(f"inputs/day{i}.txt", "r") as f:
		data = f.read()

	return data.split('\n')[:-1]
