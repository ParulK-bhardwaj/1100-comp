''''
Welcome to Jess + Joi's Dog Kennel 🦴

Every dog is stored at an index

For example: 
index 0 Henry. 🐕‍🦺
index 2 Wuffles. 🐕
'''

# List of dog names

dogs = ["Henry", "Rookie", "Wuffles", "Nugget"]


# Print the first dog's name 
print(dogs[0])

# TODO: Print the second dog
print(dogs[1])

# TODO: Print the third dog
print(dogs[2])



# TODO: Print the fouth dog
print(dogs[3])


# TODO: Use negative indexing to print the last dog
print(dogs[-1])

# TODO: Use negative indexing to print the names of the other dogs
print("checking")
print(dogs[-4:-1])

# Joi and Jess want to split up the work at the kennel. Using list 
# slicing, assign Joi two dogs

# listname[start:stop]

joi_dogs = dogs[0:2]
print(joi_dogs)

# TODO: Assign jess the remaining dogs and print Jess' dogs
jess_dogs = dogs[2:4]
print(jess_dogs)
# TODO: A new dog is visiting the kennel. Make up a name and 
# append that dog to the list use: dogs.append("Name")

dogs.append("Woolf")

# TODO: Print the dogs list to check the dogs. 

print(dogs)
# num_visit stores the number of times a dog has visited the kennel
num_visit = [2, 3, 5, 2]

# TODO: The new dog just visited for the first appead a 1 to the 
# num_visits list:

num_visit.append(1)

# TODO: Print each dog and the number of times it has visited: 
print(f"{dogs[0]} has visited {num_visit[0]}")
print(f"{dogs[1]} has visited {num_visit[1]}")
print(f"{dogs[2]} has visited {num_visit[2]}")
print(f"{dogs[3]} has visited {num_visit[3]}")
print(f"{dogs[4]} has visited {num_visit[4]}")
# TODO: Put the code above into a function that will print the
# dogs and visits
def dog_visit(dogs, num_visit):
    for i in range(len(dogs)):
        for num in num_visit:
            dogs_match_num = (f"{dogs[i]} has visited {num_visit[num]}")
    print(dogs_match_num)

print("function check")
print(dog_visit)


# TODO: Imagine it's a new week and the dog's have all visited one 
# more time. Increase each dog's visit by 1
num_visit[0] += 1 # add one to Henry's visits
# num_visit[0:5] += 1
print("\ncheck")
print(num_visit)

["Henry", "Rookie", "Wuffles", "Nugget"]
# add 1 to Rookie
# add 1 to Wuffles
# add 1 to Nugget

# TODO: Print the names and visits of all dogs again! 



# TODO: Count the dogs in the list with code! Use len()
# to print the number of dogs in the list: len(dogs)


# TODO: Write a function that takes the index of a dog
# and prints name of the dog and the number of visits. 


# TODO: Modify your function above, the one that prints 
# all of the dogs, to use this function!


# TODO: The kennel is doing well. We need to know how much 
# money we are making sittting dogs. Look up the amount 
# a kennel might charge for sitting a dog per day. I found
# $21 to $40. Define a variable cost_per_day. 


# TODO: Write a function that returns the amount made for 
# sitting a dog. This function should take the index of the
# dog as a parameter and return the num_visit for that dog 
# times the cost_per_day. 


# TODO: Using the function you created in the previous 
# step print a billing message for each dog. Include the 
# dog's name, the number of visits, cost per visit, and 
# the total bill: 


# TODO: Print a billing message for each dog in your list: 

