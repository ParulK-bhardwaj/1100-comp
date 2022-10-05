def greet_by_name(name):
	greeting = "Hello, " + name + "!"
	return greeting

a = greet_by_name("Amy")
b = greet_by_name("Bob")
c = greet_by_name("Cat")
d = greet_by_name("Dan")

# Print the variables above to the console
print(a)
print(b)
print(c)
print(d)
# What type is returned? How can you check the type? Do it that here:
print(type(a))

def add_ten(number): 
	new_number = number + 10
	return new_number

add_ten(60)
add_ten(30)
e = add_ten(60)
f = add_ten(30)

# How can you save the values returned by the add_ten function? 
print(e)
print(f)
# Print the values returned by the two calls to add_ten above:

print(add_ten(e + f))
# Use add_ten to add 10 to the total of the first two calls to add_ten. 
# The answer should be 120. Print the result below. 

