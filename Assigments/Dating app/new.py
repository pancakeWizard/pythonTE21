def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()

userFile = open("Assigments/Dating app/tables/userLogin.txt", "r+")
passFile = open("Assigments/Dating app/tables/userPass.txt", "r+")
personsFile = open ("Assigments/Dating app/tables/persons.txt","r+")


users = userFile.readlines()
passwords = passFile.readlines()
persons = personsFile.readlines()

cleanUserData(users,users)
cleanUserData(passwords,passwords)

def auth(login, password):
    print(login)
    print(password)
    while True:
        currentUser = input("Enter your login: ").lower()
        if currentUser in login:
            for i in range(0,len(login)):
                if currentUser == login[i]:
                    print("Hilow hilow")
                    while True:
                        keyWord = input("Enter your password: ").lower()
                        if keyWord == password[i]:
                            print(f"Welcome, {currentUser}")
                            break
                        else:
                            wrongPass = input("Wrong password. \n1. Try again \n2. Exit \n")
                            if wrongPass == "1":
                                continue
                            else: 
                                break
        else:
            inp = input(f"There is no user {currentUser}. \n1. Try again \n2. Exit \n")
            if inp == "1":
                continue
            else:
                break
        break

def signUp(login, password):
    print(login)
    while True:
        newUser = input("Create your login: ").lower()
        if newUser in login:
            inp = input(f"Account {newUser} already exist.\n1. Try again.\n2. Log in\n")
            if inp != "2":
                continue
            else:
                auth(users, password)
                break
        else:
            userFile.write(f"\n{newUser}")
            break

    while True:
        newPassword = input("Create your password: ")
        newPasswordConf = input("Confirm your password: ")
        if newPassword != newPasswordConf:
            print("You enter two diffrent passwords. Try again! ")
        else:
            passFile.write(f"\n{newPasswordConf}")
            break
    
    while True:
        newName = input("Enter your first and second name: ")
        if not newName == "" or " " or "\n":
            personsFile.write(f"\n{newName}")
            break
        else:
            print("You may not have empty name. Try again!")
    
    
signUp(users, passwords)

userFile.close()
passFile.close()