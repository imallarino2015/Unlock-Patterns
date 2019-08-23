def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]

def generatePattern(fileName):
	coordinates = [
		"(0,0)", "(0,1)", "(0,2)",
		"(1,0)", "(1,1)", "(1,2)",
		"(2,0)", "(2,1)", "(2,2)"
	]
	with open(fileName,"w+") as f:
		row=""
		for p in permute([0, 1, 2, 3, 4, 5, 6, 7, 8]):
			for i in range(len(p)):
				row += "\"" + str(p[i]) + "\"" + ("," if (i<len(p)-1) else "\n")
		f.write(row)