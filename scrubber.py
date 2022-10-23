import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge


# Cleaning the data by handling the missing data
def clean_up(df):
	
	# Identifying the columns having missing data
	null_columns=df.columns[df.isnull().any()]
	# Handling the columns which have more than 50% missing data
	threshold=int(df.shape[0]*0.5)
	drop_columns=[column for column in null_columns if df[column].isnull().sum()>=threshold]
	df=df.drop(labels=drop_columns,axis=1,errors='ignore')
	null_columns=null_columns.drop(labels=drop_columns)

	# Handling the columns with lesser missing data
	data=df

	# Categorical data
	categorical=[col for col in null_columns if df[col].dtype=='object']
	if len(categorical)>0:
		data1=data.drop(labels=[col for col in data.columns if data[col].dtype!='object'],axis=1,errors='ignore')		
		imp=SimpleImputer(missing_values=np.nan,strategy='most_frequent') #can be mean, median or constant also
		imputed_df=imp.fit_transform(data1)
		imputed_df=pd.DataFrame(imputed_df,columns=data1.columns)
		for col in imputed_df.columns:
			df[col]=imputed_df[col]

	# Continuous data
	data2=df.drop(labels=[col for col in data.columns if data[col].dtype=='object'],axis=1,errors='ignore')
	imp=IterativeImputer(BayesianRidge())
	imputed_df=imp.fit_transform(data2)
	imputed_df=pd.DataFrame(imputed_df,columns=data2.columns)
	for col in imputed_df.columns:
		df[col]=imputed_df[col]

	return df