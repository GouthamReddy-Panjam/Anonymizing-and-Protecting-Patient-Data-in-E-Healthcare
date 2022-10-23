import pandas as pd

#Collecting the list of explicit identifiers
df=pd.read_csv("./list/ei_list.txt").values.tolist()
EI_LIST=[j for i in df for j in i]

# Masking the columns containing explicit identifiers
def mask(df):
	headers=list(df.columns)
	for header in headers:
		for ei in EI_LIST:
			if header.lower().strip().replace('"','').replace("'",'').replace('-','').replace('_','').replace(' ','').find(ei)!=-1:
				df[header]='#'
	return df