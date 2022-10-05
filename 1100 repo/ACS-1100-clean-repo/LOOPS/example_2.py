'''
Use while loops to solve the problems below.
'''


# TODO - Exercise 1: Repeatedly print the value of the variable price,
# decreasing it by 0.7 each time, as long as it remains positive.

price = 5

while price > 0: 
    print(f"Price: {price}")
    price -= 0.7
   



# TODO - Exercise 2: Print ONLY even numbers from 0 to 20
number =0 
while number <= 20 and number %  2 ==  0:
    print(f"Even Number: {number}")
    number += 1

