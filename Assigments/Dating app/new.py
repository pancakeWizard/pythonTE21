def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()

userFile = open("Assigments/Dating app/tables/userLogin.txt", "r+")
passFile = open("Assigments/Dating app/tables/userPass.txt", "r+")
personsFile = open ("Assigments/Dating app/tables/persons.txt","r+")
sexFile = open("Assigments/Dating app/tables/sex.txt","r+")
prefFile = open ("Assigments/Dating app/tables/preferences.txt","r+")

sexes = sexFile.readlines()
users = userFile.readlines()
passwords = passFile.readlines()
persons = personsFile.readlines()
preferences = prefFile.readlines()

cleanUserData(users,users)
cleanUserData(passwords,passwords)
cleanUserData(sexes, sexes)
cleanUserData(preferences,preferences)

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
        if newUser in login or not newUser.isalnum():
            nextUser = input(f"Account {newUser} already exist or you are trying to create empty username.\n1. Try again.\n2. Log in\n3. Exit\n")
            if nextUser == "3":
                return
            elif nextUser != 2:
                continue
            else:
                auth(users, password)
                return
        else:
            break

    while True:
        newPassword = input("Create your password: ")
        newPasswordConf = input("Confirm your password: ")
        if newPassword != newPasswordConf or not newPassword.isalnum():
            nextPass = input("You enter two different passwords or trying to create an empty password.\n1. Try again\n2. Exit\n")
            if nextPass != 2:
                continue
            else:
                return
        else:
            break
    
    while True:
        newName = input("Enter your first and second name: ")
# newName.isalnum() returns true if the string is spaces. I don't want to allow users to enter just spaces or enter to skip questions.
# I took this function from stackoverflow. I could use "or newName == ' ' or newName == '  '", but it's not too logical to try
#guess how many times the user will type space.
# (https://ru.stackoverflow.com/questions/1414806/python-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%BF%D0%BE%D0%BB%D1%8F-%D0%B2%D0%B2%D0%BE%D0%B4%D0%B0)
        if len(newName) == 0 or not newName.isalnum():
            nextName = input("You may not have empty name.\n1. Try again\n2. Exit\n")
            if nextName == "1":
                continue
            else:
                return
        else:
            break
    
    while True:
        newSex = input("What is your gender?\n1. Male\n2. Female\n4. Other\n")
        if not newSex.isalnum():
            nextSex = input("You are trying to create an empty gender.\n1. Try again\n2. Exit\n")
            if nextSex != "2":
                continue
            else:
                return
        elif newSex != "1" or "2":
            print("Your gender is changed to 4 (other)")
            newSex = "4"
            break
        else:
            break
    
    while True:
        newPref = input("Choose which gender would you like to date?\n1. Male\n2. Female\n3. Both\n4. Other\n")
        if newPref != "1" or "2" or "3" or "4" or not newPref.isalnum():
            nextPref = input("You may not skip this question.\n1. Try again\n2. Exit\n")
            if nextPref != "2":
                continue
            else:
                return
        else:
            break
        

        
            
        
#this section will write all the data about the user to "database files" if the user doesn't break signing up.
#But if the user breaks the process, no data will be written.
    if True:
        # userFile.write(f"\n{newUser}")
        # passFile.write(f"\n{newPasswordConf}")
        # personsFile.write(f"\n{newName}")
        # sexFile.write(f"\n{newSex}")
        # preferences.write(f"\n{newPref}")
        pass
            
    
    
signUp(users, passwords)

userFile.close()
passFile.close()
personsFile.close()
sexFile.close()
