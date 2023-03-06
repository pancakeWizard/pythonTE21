def auth():
    with open("Assigments/Dating app/tables/userLogin.txt", "r") as users:
        usersList = users.readlines()
        for user in usersList:
            user = user.replace(' ', '')
            user= user.replace('\n','')
    with open("Assigments/Dating app/tables/userPass.txt", "r") as pas:
        passList = pas.readlines()
    userLogin = input("Enter your login ")
    if userLogin in usersList:
        for i in range (0,len(usersList)):
            if userLogin == usersList[i]:
                while True:
                    current_pass = input("Enter your password: ")
                    if not current_pass == passList[i]:
                        print("Wrong password. Try again!")
                    else:
                        print(f"Welcome, {userLogin}!")
                        break
    else:
        print(f"There is no user {userLogin}. Reload app to sign up or try again.\n")

start = int(input("""Welcome to our dating app!
1. Log in
2. Create an account
"""))
if start == 1:
    auth()
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
    auth()
