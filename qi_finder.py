import pandas as pd
from statistics import mean

#Collecting the list of quasi identifiers
df=pd.read_csv("./list/qi_list.txt").values.tolist()
QI_LIST=[j for i in df for j in i]

# Calculation of threshold
def threshold_calculator():
	parameters=[ 	{'yes':0,'no':-0.3},
					{'yes':-0.5,'no':0},
					{1:-0.1, 2:-0.2, 3:-0.3, 4:-0.4, 5:-0.5} 
	]
	threshold=0.15

	trust=input('Is the receiver of the data a trusted organization? Yes/No : ')
	linkage_possibility=input('Is our data such that public resources might have related information? Yes/No : ')
	working_period=int(input('What is the working period given by the organization for this data?\n\
1) Less than 1 year\n2) Between 1 year and 3 years\n3) Between 3 years and 6 years\n4) Between 6 years and 9 years\n5) More than 10 years\n'))
	
	inputs=[trust,linkage_possibility,working_period]
	error=False
	if trust.lower() in ['yes','no'] and linkage_possibility.lower() in ['yes','no'] and working_period in range(1,6):
		for i,parameter in zip(inputs,parameters):
			threshold+=parameter[i]
	else:
		error=True

	return error,threshold

# Masking the columns containing quasi identifiers
def find_qi(df):
	headers=list(df.columns)
	
	# Check for primary quasi-identifiers
	primary_qi=[]
	for header in headers:
		for qi in QI_LIST:
			if header.lower().strip().replace('"','').replace("'",'').replace('-','').replace('_','').replace(' ','').find(qi)!=-1:
				primary_qi.append(header)

	# Check for secondary quasi-identifiers
	error,threshold=threshold_calculator()
	secondary_qi=[]
	
	if not error:
		total_count=df.count()
		total_equivalence_classes=df.drop_duplicates(subset=None,keep='first',inplace=False).shape[0]

		risk={}

		for qi in primary_qi:
			# Checking the uniqueness of primary quasi-identifiers
			no_of_unique=[i for i in df[qi].value_counts() if i==1]
			uniqueness=len(no_of_unique)/total_count[qi]

			# Checking the influence of primary quasi-identifiers on the data
			cols=list(df.columns)
			cols.remove(qi)
			no_of_equivalence_class_without_qi=df.drop_duplicates(subset=cols,keep='first',inplace=False).shape[0]
			influence=1-(no_of_equivalence_class_without_qi/total_equivalence_classes)
		
			# Calculating the risk
			risk[qi]=mean([uniqueness,influence])
		
		secondary_qi=[qi for qi in risk if risk[qi]>=threshold]
	
	return error,secondary_qi