'''
Before Sunday Night Football, you want to go shopping for your favorite snacks! 

Let's create a shopping list with your favorite snacks to eat!
'''

#TODO: create a list of strings containing your favorite snacks
snack_list = [
    'chips\n',
    'nacho\n',
    'veggie sticks\n',
    'bruchetta\n',
    'grilled cheese\n',
    'popcorn\n'
]

#TODO: open a new file called "shopping_list.txt" for write
output_file_name = "shopping_list.txt"

outfile = open(output_file_name, "w")

for snack in snack_list:
    entry = outfile.writelines(snack)
print(entry)
outfile.close()

# #TODO: finish this loop to write your favorite snacks to the shopping_list.txt file
# for snack in snack_list:  
#   outfile.write(snack)

# outfile.close()


# Notice how the above code overwrites the data with each loop. 
# Let's modify our code to write multiple lines of code to the file!


'''
TODO: 

1. Creating a function called write_shopping_list() that has one parameter called snacks. This function takes a list of strings.

2. You function should write to the file using .writelines() 

'''

fav_snacks = [
    'Potato chips\n',
    'Nacho salsa\n',
    'cookies\n',
    'sandwich\n' 
]

output_file = 'shopping_list.txt'

outfile2 = open(output_file, 'w')

outfile2.writelines(fav_snacks)

outfile2.close