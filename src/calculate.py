import pandas as pd

def trim(data,colName):
	data = data.drop(str(colName), axis=1)
	data = data.drop_duplicates()
	return data

def count(fileName):
	data = pd.read_csv(fileName)
	data = data[data.isValid]

	total = 0
	total = total + data.shape[0]

	for i in reversed(range(4,9)):
		data = trim(data, i)
		total = total + data.shape[0]

	return total