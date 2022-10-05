'''
Function Practice: 

modify the code you just wrote by 
creating a function called read_candy() 
that takes in the file name as a parameter 
and returns the lines of the file as a list
'''

# STEP 1: Store the name of the file
# TODO: define a variable filename and store the name 
# of the file cand.txt. Ask yourself what the path 
# should be? 



def read(input_file_name):
  infile = open(input_file_name,"r")
  lines = infile.readlines()
  infile.close()
  return lines

# from msilib.schema import IniFile


# def read(filename):
#   # Open
#   infile = open(filename, 'r')

#   # Read
#   lines = infile.readlines()

#   #Close
#   infile.close()

#   # Return
#   return lines

#TODO: print out all the lines of the candy file

input_file_name = "candy.txt"
print(read(input_file_name))

# candy_lines = read('candy.txt')
# print(candy_lines)

# TODO: Function Practice: modify the code you just wrote 
# by creating a function called read_candy() that takes in 
# the file name as a parameter and returns the lines of the 
# file as a list


# TODO: Read the file flavors.txt Print all of it's lines
# file_name = "flavors.txt"
print(read("flavors.txt"))
