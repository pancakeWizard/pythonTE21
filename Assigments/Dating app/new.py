def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()

interestsList = ["games", "travel", "music", "dance", "films", "food", "cars", "animals", "architecture", "IT", "sport", "books"]

userFile = open("Assigments/Dating app/tables/userLogin.txt", "r+")
passFile = open("Assigments/Dating app/tables/userPass.txt", "r+")
personsFile = open ("Assigments/Dating app/tables/persons.txt","r+")
sexFile = open("Assigments/Dating app/tables/sex.txt","r+")
prefFile = open ("Assigments/Dating app/tables/preferences.txt","r+")
interFile = open("Assigments/Dating app/tables/interests.txt", "r+")
ageFile = open ("Assigments/Dating app/tables/age.txt", "r+")

users = userFile.readlines()
passwords = passFile.readlines()
sexes = sexFile.readlines()
persons = personsFile.readlines()
preferences = prefFile.readlines()
interests = interFile.readlines()
ages = ageFile.readlines()

cleanUserData(users,users)
cleanUserData(passwords,passwords)
cleanUserData(sexes, sexes)
cleanUserData(persons, persons)
cleanUserData(preferences,preferences)
cleanUserData(ages, ages)

def auth(login =users, password =passwords):
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
                            if wrongPass != "2":
                                continue
                            else: 
                                return
        else:
            inp = input(f"There is no user {currentUser}. \n1. Try again \n2. Exit \n")
            if inp != "2":
                continue
            else:
                return
        break
    return(currentUser)

def signUp(login =users, password =passwords):
    print(login)
    while True:
        newUser = input("Create your login: ").lower()
        if newUser in login or not newUser.isalnum() or newUser == "reserved":
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
        newName = input("Enter your first name: ")
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

 #this part will be improved with help of try except in future version.   
    while True:
        newSex = input("What is your gender?\n1. Male\n2. Female\n4. Other\n")
        if not newSex.isalnum():
            nextSex = input("You are trying to create an empty gender.\n1. Try again\n2. Exit\n")
            if nextSex != "2":
                continue
            else:
                return
        if newSex != "2" and newSex != "1":
            print("Your gender is changed to 4 (other)")
            newSex = 4
            break
        else:
            break
        
 #this part will be improved with help of try except in future version.   
    while True:
        newPref = input("Choose which gender would you like to date?\n1. Male\n2. Female\n3. Both\n4. Other\n")
        if newPref != "1" and newPref != "2" and newPref != "3" and newPref != "4" and not newPref.isalnum():
            nextPref = input("You may not skip this question.\n1. Try again\n2. Exit\n")
            if nextPref != "2":
                continue
            else:
                return
        else:
            break

#this part will be improved with help of try except in future version.
    while True:
        newAge = input("Enter your age: ")
        if not newAge.isalnum():
            nextAge = input("You may not skip this question.\n1. Try again\n2. Exit\n")
            if nextAge != "2":
                continue
            else:
                return
        else:
            break

#This part will be improved with help of try except in future versions. There is a problem now: if user will enter an empty intress
##then the database system will not work anymore. Due to the fact that there is no way to control it and overwrite file without a big piece of code with
#a lot of comparisons that I don't think are as necessary in this version I will improve it in an easier way during develompent of the second versin 
#by using try-catch
    interFile.write("\n")
    while True:
        if input("Write \"add\" to add an intress or \"done\" to confirm your interests: ").lower() == "add":
            for i in range(0,len(interestsList)):
                print(f"{i}. {interestsList[i]}")
            newInteres = input("Choose an interes from the list above. T.ex. 1 or 5: ")
            if not newInteres.isalnum():
                nextInter = input("You may not skip this question.\n1. Try again\n2. Exit\n")
                if nextInter != "2":
                    continue
                else:                       
                    return   
            else:
                interFile.write(f"{newInteres} ")
        else:
            break
#this section will write all the data about the user to "database files" if the user doesn't break signing up.
#But if the user breaks the process, no data will be written.
    userFile.write(f"\n{newUser}")
    passFile.write(f"\n{newPasswordConf}")
    personsFile.write(f"\n{newName}")
    sexFile.write(f"\n{newSex}")
    prefFile.write(f"\n{newPref}")
    ageFile.write(f"\n{newAge}")
    return(True)

def searchMachine(user):
    if user == "reserved":
        print("You need to log in before you can start us the app.")
        return
    else:
        for login in users:
            if user == login:

                pass

def chat():
    pass

def mainMenu():
    loginAs = "reserved"
    while True:
        mainState = input("Welcome to our dating app! \n1. Log in\n2. Sign up\n3. Find best matches\n4. Open chat\n5. Exit\n")
        if mainState == "1":
            loginAs = auth(users,passwords)
            continue
        elif mainState == "2":
            isSignedUp = signUp()
            if isSignedUp:
                print("You are successfully signed up! Start using our app by Log in.")
            continue
        elif mainState == "3":
            searchMachine(loginAs)
            continue
        elif mainState == "4":
            chat(loginAs)
            continue
        elif mainState == "5":
            break
        return

mainMenu()

userFile.close()
passFile.close()
personsFile.close()
sexFile.close()
prefFile.close()
interFile.close()
ageFile.close()