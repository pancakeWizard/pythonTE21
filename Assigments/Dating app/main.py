application = 0

def auth(users):
    userLogin = input("Enter your login ")
    for i in range (0,len(users)):
        if userLogin in users[i]:
            current_user = i
    while True:
        current_pass = input("Enter your password: ")
        if not current_pass in users[current_user]:
            print("Wrong password. Try again!")
        else:
            print(f"Welcome, {userLogin}!")
            return(2)

if application == 0:
    with open("Assigments/Dating app/tables/users.txt", "r") as users:
        usersList = users.readlines()
        start = int(input("""Welcome to our dating app!
1. Log in
2. Create an account
"""))
    if start == 1:
        application = auth(usersList)
    elif start == 2:
        newLogin = input("Enter you Name: ")
        with open("Assigments/Dating app/tables/users.txt", "a") as usersFile:
            usersFile.write(f"\n{newLogin}")
        while True:
            newPassword = input("Create your password ")
            newPasswordConf = input("Confirm your password ")
            if newPassword != newPasswordConf:
                print("You enter two diffrent passwords. Try again! ")
            else:
                with open("Assigments/Dating app/tables/users.txt", "a") as usersFile:
                    usersFile.write(f" {newPasswordConf}")
                break
        print(f"Welcome, {newLogin}!")
        application = 1
# elif application == 1:

