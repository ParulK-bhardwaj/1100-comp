#TODO: Using a for loop, print out each color from the list 
# called colors.
colors = ["red", "orange", "green", "blue", "purple"]
       # [    0,        1,        2,     3,        4]
          

for color in colors:  
  print(color)

# For however many colors are in the list called colors
# exectute this for loop
for i in range(len(colors)):
  color = colors[i]
  print(color + " is awesome!") 




#TODO: Create a list of 4 names.
#TODO: Using a for loop, print out each name with " is 
# awesome!" added after each name.
tryName = ['A', 'B', 'C', 'D']

for name in tryName:
  print(f"{name} is awesome!") 



#TODO: create a list of five integers
#TODO: print the sum of the numbers in the list

integers = [ 1, 2, 3, 4, 5]
total = 0
for integer in integers:
  total = total + integer
print(total)

print(sum(integers))





#TODO: After calulcating the sum, calculate the average.
# To calculate average, we take the sum divided by the 
# number of elements in the list called numbers

avg = total/ len(integers)

print(avg)

for integer in integers:
  average = total / len(integers)
print (average)

# Redo these with range() 

