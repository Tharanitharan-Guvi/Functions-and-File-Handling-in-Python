'''
Login and Signin System:

database = {}
username -> key
password -> value


1. Value from the user (1, 2)
2. If they have typed the input is 1 --> Signin
                                   2 --> Login
3. If the input == 1:
    username = 
    password =
    store them in the database
    print("Successfully Signed in")

4. if the input == 2:
    username = 
    password =

    if currusername, currpassword matches up in the dictionary/database
    
    if both the password matches --> successfully logged in
    else --> incorrect password
    
    if the username is not at all present in the database/dictioanry:
    print("Please sign-in first")
    '''


def signin(username, password):
    database[username] = password
    print("Successfully signed in")    

def login(username, password):
    if username in database:
        if password == database[username]:
            print("Successfully Logged in")
        else:
            print("Incorrect password. Try again.")
    else:
        print("Please signin first.")


database = {}
while True:
    print("1. Signin  2. Login  3. Exit")
    option = int(input("Enter your option:  "))

    if option == 3:
        break

    elif option == 1:
        username = input("Username: ")
        password = input("Password: ")

        signin(username, password)
    
    elif option == 2:
        username = input("Username: ")
        password = input("Password: ")
        login(username, password)
    
    print()
    print("---------------------------------------------")
    print()

print("Thanks for connecting with us")