import pandas as pd

import generate
import validate
import calculate
import visualize

if __name__ == "__main__":
	visualize.createImage("../cover.png",[])

	generate.generatePattern("../data/data.csv")
	validate.validate("../data/data.csv","../data/validated.csv")
	print(calculate.count("../data/validated.csv"))

	df=pd.read_csv("../data/validated.csv")
	df = df[df.isValid]
	df = df.drop("isValid", axis=1)

	for i in reversed(range(3,9)):
		print(df.head())
		print(df.shape[0])
		for idx, row in df.iterrows():
			visualize.createImage(
				"../pics/" + str(len(row)) + "/" +
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
