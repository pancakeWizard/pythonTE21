def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()
        

def genderData(array, newArray):
    for i in range (len(array)):
        if newArray[i] == "male":
            newArray[i] = 1
        elif newArray[i] == "female":
            newArray[i] = 2
        else:
            newArray[i] = 3

genderSearch = int(input("""Who would you like to date?
1. Male
2. Female
3. Other
"""))
def searchMachine(currentUser, genderSearch):
    with open ("Assigments/Dating app/tables/sex.txt", "r") as sex:
        sexes = sex.readlines()
        cleanUserData(sexes,sexes)
        genderData(sexes,sexes)
        print(sexes)

    with open ("Assigments/Dating app/tables/preferences.txt","r") as preferences:
        pref = preferences.readlines()
        cleanUserData(pref,pref)
        genderData(pref,pref)

    sexFirstMatch = []
    sexDoubleMatch = []
    sexMatch = []
    for i in range(0, len(sexes)):
        if sexes[i] == genderSearch:
            sexFirstMatch.append(i)
            if currentUser in sexFirstMatch:
                sexFirstMatch.remove(currentUser)
    for l in range(0, len(pref)):
        if pref[l] == sexes[currentUser]:
            sexDoubleMatch.append(l)
    for f in range(0, len(sexFirstMatch)):
        for s in range(0, len(sexDoubleMatch)):
            if sexFirstMatch[f] == sexDoubleMatch[s]:
                sexMatch.append(sexFirstMatch[f])
    # print(sexFirstMatch)
    # print(sexes[currentUser])
    # print(sexDoubleMatch)
    # print(sexMatch)

    with open ("Assigments/Dating app/tables/age.txt", "r") as age:
        ages = age.readlines()
        cleanUserData(ages,ages)
        agesOfMatch = []
        for a in range(0, len(sexMatch)):
            agesOfMatch.append(ages[sexMatch[a]])  
        print(agesOfMatch)
    with open("Assigments/Dating app/tables/agePref.txt", "r") as prefAge:
        prefAges = prefAge.readlines()
        cleanUserData(prefAges, prefAges)
        prefAgesOfMatch = []
        for q in range(0, len(sexMatch)):
            prefAgesOfMatch.append(prefAges[sexMatch[q]])  
        print(prefAgesOfMatch)

    

    nextStep = input(f"""We found {len(sexMatch)} persons for you. Would you like to see their profiles? 
1. Yes
2. No
3. Next question
""")
    if nextStep == "1":
        showProfile()
    elif nextStep == "2":
        return
    else:
        if sexMatch != []:
            pass
        else:
            print("There is no matches. Sorry :(")
    

searchMachine(3, genderSearch)

def showProfile(account):
    pass