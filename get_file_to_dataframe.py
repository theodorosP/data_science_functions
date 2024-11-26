import pandas as pd

def read_file_to_dataframe(file_to_read):
	dataframe = pd.read_csv(file_to_read, sep="\s+", header=None, skipinitialspace=True, skiprows=0, skipfooter=0, engine="python")
	return dataframe
