def formatListToCSV(l):
	s=""
	for item in l:
		s+="\""+str(item)+"\","
	s=s[:-1]
	return s
	# return "\""+str(l).replace("[","").replace("]","").replace("\'","").replace(", ","\",\"").strip()+"\""

def formatCSVToList(s):
	l=[]
	items=s.split(",")
	for item in items:
		if item.startswith("\'") or item.startswith("\""):
			item=item[1:]
		if item.endswith("\'") or item.endswith("\""):
			item=item[:-1]
		l.append(item)
	return l

def isConsecutive(valueList,orderedItems):
	return formatListToCSV(orderedItems) in formatListToCSV(valueList)

def getValidity(li,state):
	valOrders=[
		["0","1","2"],	# Rule 1: No 0 <-> 2 without 1
		["3","4","5"],	# Rule 2: No 3 <-> 5 without 4
		["6","7","8"],	# Rule 3: No 6 <-> 8 without 7
		["0","3","6"],	# Rule 4: No 0 <-> 6 without 3
		["1","4","7"],	# Rule 5: No 1 <-> 7 without 4
		["2","5","8"],	# Rule 6: No 2 <-> 8 without 5
		["0","4","8"],	# Rule 7: No 0 <-> 8 without 4
		["2","4","6"]	# Rule 8: No 2 <-> 6 without 4
	]
	for v in valOrders:
		if isConsecutive(li, [v[0], v[2]]):
			for item in li:
				if str(item) == v[1]:
					break
				if str(item) == v[2]:
					return False
		if isConsecutive(li, [v[2], v[0]]):
			for item in li:
				if str(item) == v[1]:
					break
				if str(item) == v[0]:
					return False
	return state

def validate(inFileName,outFileName):
	with open(inFileName,"r") as inFile:
		with open(outFileName,"w+") as outFile:
			outFile.write("\"0\",\"1\",\"2\",\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"isValid\"\n")
			for line in inFile.readlines():
				lineItems=line.replace("\"","").replace("\n","").split(",")
				isValid=True
				isValid=getValidity(lineItems, isValid)
				outFile.write(line.replace("\n","")+","+str(isValid)+"\n")