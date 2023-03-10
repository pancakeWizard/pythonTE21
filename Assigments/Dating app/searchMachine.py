def cleanUserData(array,newArray):
    for i in range (len(array)):
        newArray[i] = newArray[i].replace(' ','')
        newArray[i] = newArray[i].replace('\n','')
        newArray[i] = newArray[i].lower()
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
        print(sexes)

    with open ("Assigments/Dating app/tables/preferences.txt","r") as preferences:
        pref = preferences.readlines()
        cleanUserData(pref,pref)

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
    print(sexFirstMatch)
    print(sexes[currentUser])
    print(sexDoubleMatch)
    print(sexMatch)

searchMachine(7, genderSearch)

