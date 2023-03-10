def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()



genderSearch = int(input("""Who would you like to date?
1. Male
2. Female
3. Other"""))
def searchMachine(currentUser, genderSearch):


    with open ("Assigments/Dating app/tables/sex.txt", "r") as sex:
        sexes = sex.readlines()
        cleanUserData(sexes,sexes)
        print(sexes)
    sexFirstMatch = []
    sexDoubleMatch = []
    sexMatch = []
    if genderSearch == 1:
        for i in range(0, len(sexes)):
            if sexes[i] == "male":
                sexFirstMatch.append(i)
                if currentUser in sexFirstMatch:
                    sexFirstMatch.remove(currentUser)

        with open ("Assigments/Dating app/tables/preferences.txt","r") as preferences:
            pref = preferences.readlines()
            cleanUserData(pref,pref)
        for i in range(0, len(pref)):
            if pref[i] == sexes[currentUser]:
                sexDoubleMatch.append(i)
    
        for f in range(0, len(sexFirstMatch)):
            for s in range(0, len(sexDoubleMatch)):
                if sexFirstMatch[f] == sexDoubleMatch[s]:
                    sexMatch.append(sexFirstMatch[f])
    print(sexFirstMatch)
    print(sexes[currentUser])
    print(sexDoubleMatch)
    print(sexMatch)

searchMachine(0, genderSearch)

