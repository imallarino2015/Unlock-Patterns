import pandas as pd

import generate
import validate
import calculate
import visualize

if __name__ == "__main__":
	# visualize.createImage("../pics/test.png",[3,0,6,5,8,2,4,1,7])
	# s=validate.formatListToCSV([0,1,2,3,4,5,6,7,8])
	# print(s)
	# sl=validate.formatCSVToList(s)
	# print(sl)
	# il=[]
	# for item in sl:
	# 	il.append(int(item))
	# print(il)

	# generate.generatePattern("../data/data.csv")
	# validate.validate("../data/data.csv","../data/validated.csv")
	print(calculate.count("../data/validated.csv"))

	df=pd.read_csv("../data/validated.csv")
	df = df[df.isValid]
	df = df.drop("isValid", axis=1)

	for i in reversed(range(3,9)):
		print(df.head())
		print(df.shape[0])
		for idx, row in df.iterrows():
			visualize.createImage(
				"pics/" + str(len(row)) + "/" +
				str(row.tolist()).
				replace("[", "").
				replace("]", "").
				replace(",","").
				replace(" ", "") +
				".png",
				row.tolist()
			)
		df = calculate.trim(df, i)
		df = calculate.trim(df, i)
