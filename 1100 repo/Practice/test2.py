
input_file_name = "data.txt"

def load_user_data(input_file_name):
    infile = open(input_file_name, "r")
    lines = infile.readlines()
    customer_info = []
# For loop to go through each line to generate sperate lists for 3 users. 
# used replace to remove newline from each user line and split to convert string into a list.
    for line in lines:
        customer_info.append(line.replace("\n","").split(','))
    return (customer_info)

print(load_user_data(input_file_name))

customer_info = load_user_data(input_file_name)
def prompt(username, password):
    username = input("Please enter your Username: ")
    password = input("Please enter your Password: ")
prompt           
def do_username_password_match(username, password):
    for customer in customer_info:
        if customer[0] == username and customer[1] == password:
            return True
match = do_username_password_match(username, password)

def try_again(username, password):
    while True:
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")
        if match is False:
            print("The Username or password is not correct, please try again!")
        else:
            break

try_again(username, password)

def display_user_info(username, password):
    for customer in customer_info:
        if customer[0] == username and customer[1] == password:
            return(f"Full Name: {customer[2]}\nAccount Balance: {customer[3]}")
        elif customer[0] != username and customer[1] != password:
            return("username and password not found")

print(display_user_info(username, password))


        
# def balance_check():
#     print("Welcome to Balance-Check app!")
   


    





