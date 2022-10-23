import os
import argparse
import pandas as pd
from scrubber import clean_up
from ei_handler import mask
from qi_finder import find_qi

# For running through command line
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--input-file-path", required=True,
	help="path to the input csv record file")
ap.add_argument("-o", "--output-file-name", required=True,
	help="name of the output csv file")
args = vars(ap.parse_args())
# Reading the csv record file
df=pd.read_csv(args["input_file_path"])

print('**Processing the file...**\n')

# Masking the explicit identifiers
df=mask(df)
print('**Masking of explicit identifiers completed**\n')

# Cleaning the data
df=clean_up(df)
print('**Cleaning of data completed**\n')

# Creating the ouput csv record file 
path=os.path.join(os.getcwd(),'Output_files')
if not os.path.isdir(path):
	os.mkdir(path)
output_filename=str(args["output_file_name"])
if output_filename.find('.csv')==-1:
	output_filename+='.csv'
output_file_path=os.path.join(path,output_filename)
df.to_csv(output_file_path) 
print('**Processing completed**\n')
print(f'{output_filename} has been created and saved in the Output_files directory\n')

# Identifying the quasi identifiers 
print('**Analyzing quasi identifiers...**\n')
error,risky_qi=find_qi(df) 

if not error:
	if len(risky_qi)>0:
		print('Most risky quasi identifiers which need to be anonymized in the given data: ')
		print(risky_qi)
	else:
		print('Data does not need any anonymization')
else:
	print('Could not find quasi identifiers due to error in inputs!')
