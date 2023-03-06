def auth():
    with open ("Assigments/Dating app/tables/userLogin.txt", "r") as users:
        userList = users.readlines()
    with open("Assigments/Dating app/tables/userPass.txt", "r") as key:
        keyList = key.readlines()
    for i in range (len(userList)):
        keyList[i] = keyList[i].replace(' ','')
        keyList[i] = keyList[i].replace('\n','')
        userList[i] = userList[i].replace(' ','')
        userList[i] = userList[i].replace('\n','')
        keyList[i] = keyList[i].lower()
        userList[i] = userList[i].lower()
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
                print(" :( ")
    else:
        print(f"There is no user {currentUser}. Reload app to sign up or try again.")

def signUp():
    with open ("Assigments/Dating app/tables/userLogin.txt", "r") as users:
        userList = users.readlines()
        print("Welcom to our dating app! We need some information to create your account.")
        with open ("Assigments/Dating app/tables/userLogin.txt", "a") as users:
            newUser = input("Enter your name: ")
            users.write(f"\n{newUser}")
    while True:
        newPassword = input("Create your password: ")
        newPasswordConf = input("Confirm your password: ")
        if newPassword != newPasswordConf:
            print("You enter two diffrent passwords. Try again! ")
        else:
            with open("Assigments/Dating app/tables/userPass.txt", "a") as key:
                key.write(f" {newPasswordConf}")
            break
    
auth()