#This function gets the number of lines of a big file
#file = the file we want to read it's lines
#It returs the number of lines

def get_number_of_lines(file):
	number_of_lines = sum(1 for i in open(file))
	return number_of_lines


#This function gets a number and return all of it's divisors.
#It is made to get the number of lines of a file, as input and returns  it's divisors.
#n_lines = the number of lines got from the get_number_of_lines function
#It returns a list with all the divisors of the input number
def get_divisors(n_lines):
	number_of_divisors = list()
	n = 1
	for i in range(1, n_lines + 1):
		if n_lines % n == 0:
			number_of_divisors.append(n)
		n += 1
	return number_of_divisors 


number_of_lines = get_number_of_lines(file_to_read)

#nn is the number of lines I want to remove from the begining of the file
#m is the m th element of the list div. Normaly use an m from 1 to 3. The larger the m, the larger the number of lines in the big file.
#i.e div = divisors_of_10 = [1, 2, 5, 10]. If m = len(divisors_of_10 - 1), then the chunksize = 1 (with nn= 0). This means that each dataframe will have only one row
#i.e div = divisors_of_10 = [1, 2, 5, 10]. If m = 0, then the chunksize = 10 (with nn= 0). This means that each dataframe will have only one big dataframe. So pandas might not be able to read this
div = get_divisors(number_of_lines - nn)
chunksize_ = (number_of_lines -nn)/div[m]

#this function reads a file and reurns a dictionary with the file assigned in small dataframes
def convert_huge_file_to_dataframe(file_to_read, chunksize_, rows_to_skip)
  #chunksize=chunksize will create many texfiles, similar to dataframes, but not stored as dataframes
  dataframe = pd.read_csv(file_to_read, chunksize=chunksize_, sep=" ", skiprows = rows_to_skip, header = None, skipinitialspace = True)
  a = 1
  dictionary = dict()
  for i in dataframe:
	  dictionary["df_" + str(a)] = i
	  dictionary["df_" + str(a)].index = range(0, chunksize)
	  print("Read DataFrame: ", a, " out of ", number_of_lines/chunksize)
  	a += 1
  return dictionary
