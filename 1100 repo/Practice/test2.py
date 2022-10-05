
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

customer_info = load_user_data(input_file_name)

def do_username_password_match(username, password):
    for customer in customer_info:
        if customer[0] == username and customer[1] == password:
            return True

def display_user_info(username, password):
    for customer in customer_info:
        if customer[0] == username and customer[1] == password:
            return(f"Full Name: {customer[2]}\nAccount Balance: {customer[3]}")

def balance_check():
    print("Welcome to Balance-Check app!") 
    allowed_login_attempts = 3
    login_attempts = 0
    while True:
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")
        match = do_username_password_match(username, password)     
        if match is True:
            print(display_user_info(username, password))
            return(display_user_info(username, password))
        elif match is not True:
            print("Username or password does not match!")
            login_attempts += 1
            if login_attempts == allowed_login_attempts:
                print("There are too many wrong entries, please reach out to us for further assistance or re-open the app.")
                break    


load_user_data(input_file_name)
balance_check()
