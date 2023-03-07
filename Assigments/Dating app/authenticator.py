def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()

def auth():
    with open ("Assigments/Dating app/tables/userLogin.txt", "r") as users:
        userList = users.readlines()
    with open("Assigments/Dating app/tables/userPass.txt", "r") as key:
        keyList = key.readlines()
    cleanUserData(userList,keyList)
    cleanUserData(userList,userList)
    print(userList)
    print(keyList)
    currentUser = input("Enter your login: ").lower()
    if currentUser in userList:
        for i in range(0,len(userList)):
            if currentUser == userList[i]:
                print("Hilow hilow")
                for t in range (0, 4):
                    s = 3-t
                    if s!= 0:
                        keyWord = input(f"Enter your password. You have only {s} try. ").lower()
                        if keyWord == keyList[i]:
                            print(f"Welcome, {currentUser}")
                            break
                    else:
                        print("You enter wrong password 3 times. Reload app to sign up or try again.")
    else:
        print(f"There is no user {currentUser}. Reload app to sign up or try again.")

def signUp():
    interestsList = []
    with open ("Assigments/Dating app/tables/userLogin.txt", "r") as users:
        userList = users.readlines()
        print("Welcom to our dating app! We need some information to create your account.")
        with open ("Assigments/Dating app/tables/userLogin.txt", "a") as users:
            cleanUserData(userList,userList)
            print(userList)
            while True:
                newUser = input("Create your login: ").lower()
                if newUser in userList:
                    print(f"Account {newUser} already exists. Try again.")
                else:
                    users.write(f"\n{newUser}")
                    break
    while True:
        newPassword = input("Create your password: ")
        newPasswordConf = input("Confirm your password: ")
        if newPassword != newPasswordConf:
            print("You enter two diffrent passwords. Try again! ")
        else:
            with open("Assigments/Dating app/tables/userPass.txt", "a") as key:
                key.write(f"\n{newPasswordConf}")
            break
    
    with open ("Assigments/Dating app/tables/persons.txt","a") as persons:
        newName = input("Enter your first and second name: ")
        persons.write(f"\n{newName}")

    with open ("Assigments/Dating app/tables/sex.txt","a") as sex:
        newSex = input("Enter your sex: ")
        sex.write(f"\n{newSex}")

    with open ("Assigments/Dating app/tables/preferences.txt","a") as preferences:
        newPref = input("Enter your gender preferences (male/female/other)")
        preferences.write(f"\n{newPref}")

    with open ("Assigments/Dating app/tables/interests.txt", "a") as interests:
        while True:
            if input("Write \"add\n to add an intress or \"done\" to confirm your interests: ").lower() == "add":
                newIteres = input("""Choose an interes from the list below:
1. """)

signUp()