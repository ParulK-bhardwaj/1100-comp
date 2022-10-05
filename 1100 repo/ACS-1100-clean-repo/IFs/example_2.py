# Solve all of the problems here using the in and not in operators. 

fact = "Python is the best"

print("Results from testing in operator:")
# Predict the type of each of the lines below. 
# Check your predictions by running the code 

print('Python' in fact, "True") # For example I predict True
# Add your prediction to each print statement below. 
# If your prediction doesn't match the output figure out why! 

print('Best' in fact) #True

print('Py' in fact) #True
print('n i' in fact) #True

print("\nResults from testing not in operator:")
print('Java' not in fact) #True
print('Python' not in fact) #False


# What about these? 
user_name = "Casey"
status = user_name + " are currently logged in Sat Sept. 4 2021"
# Figure out if you are logged in? 
print(user_name)

# Check status for user_name
print(user_name in status)

# Prove "hacker" is not logged in using the status message
print("hacker" in status)
# Imagine "Hacker" is the user name prove it's not in status
print("Hacker" not in status)

# Prove it's September. Prove Sept. is in status. 
print("sept" in status)

# Prove it's not November. Prove Nov. is not in status. 
print("nov" not in status)

# Prove the year is not 2020
print("2020" not in status )


# Use not the operator 

yes = True
n = not yes

print(n)


