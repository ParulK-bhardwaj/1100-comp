# Solve these problems again, but use the with keyword to close the files

# output_file_name = "candy.txt" 

# outfile = open(output_file_name, "a")
with open("candy.txt" , "a") as outfile:
  candy = ['peppermints \n', 'york \n', 'nerds\n']
  outfile.writelines(candy)


# candy = ['peppermints \n', 'york \n', 'nerds']
# outfile.writelines(candy)

# outfile.close()



# Example
with open("somefile.txt", "a") as outfile:
  mytext = ['something \n', 'to \n', 'say']
  outfile.writelines(mytext)