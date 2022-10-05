# Here is the double function

def double(number):
	new_number = (2 * number)
	return new_number

first_number = double(100)
second_number = double(25)

print(first_number) # 200
print(second_number) # 50

#TODO: Cuber. This function should multiply three numbers and return the answer

def cuber(a, b, c): 
	cube = (a * b * c)
	return cube

num_1 = cuber (3, 3, 3)
print(num_1)




# Should return 27

#TODO: Write a function to generate product

def product(a, b):
	new_product = (a * b)
	return new_product

num_1 = double (3)
num_2 = cuber (2, 2, 2)
num_3 = product (num_1, num_2)
print(num_3)
# double 3 and cube 2 and return the product


