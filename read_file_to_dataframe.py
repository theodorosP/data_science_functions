#This function reads a file to dataframe with correct number of columns
#file_to_read = the file that we want to read
#sep = "something" says to ignore the "something" in order to make columns.  sep = "\s+" means to denote one or more spaces
#skiprows gives the number of rows to skip from the begining of the file
#header = None means that there is no header. By doing this, the first line moves one row down. In this way there are names in each column, like 0, 1, 2, 3...
# skipinitialspace = True skip spaces after delimeter 
#skipfooter=n, engine = "python" these two skip the last n lines of the file, they should be used todether

def read_file_to_dataframe(file_to_read):
  import pandas as pd
  dataframe = pd.read_csv(file_to_read,  sep = "\s+", skiprows = 2, header = None, skipinitialspace = True, skipfooter=4, engine = "python")
  return dataframe
