

def match_ends(s):
	counter = 0
	for string in s:
		if len(string) > 1 and string[0] == string[-1]:
			counter += 1

	return counter



