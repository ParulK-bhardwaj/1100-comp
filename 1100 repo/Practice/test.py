# function to load data. Parameter: file name, returns a list of users.
# input_file_name = "data.txt"

# # def load_data(file_name):
# infile = open(input_file_name, "r")

# # load_data(input_file_name)

file_name = 'data.txt'
with open(file_name) as line:
        aman = line.readline().split(',')
        betho = line.readline().split(',')
        camcam = line.readline().split(',')


# for line in infile:
#     if "aman" in line:
#        aman =  line.split(",") 
#        print(aman)
#     elif "betho" in line:
#         betho = line.split(",")
#         print(betho)
#     elif "camcam" in line:
#         camcam = line.split(",")
#         print(camcam)



username = input("Please enter your Username: ")
password = input("Please enter your Password ")



def display(username, password):
    if username == aman[0] and password == aman[1]:
        print(f"Full Name: {aman[2]}")
        print(f"Account Balance: {aman[3]}")
    elif username == betho[0] and password == betho[1]:
        print(f"Full Name: {betho[2]}")
        print(f"Account Balance: {betho[3]}")
    elif username == camcam[0] and password == camcam[1]:
        print(f"Full Name: {betho[2]}")
        print(f"Account Balance: {betho[3]}")
    else:
        print("User name and password not found")

display(username, password)

# def is_username_password_found():
#     if display(username, password) == "User name and password not found":
#        return True
    
# is_username_password_found()    

