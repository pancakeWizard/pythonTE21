with open('log.txt','a') as writeFile:
    toLog = input("What do you want to write to the log? ")
    writeFile.write("\n"+toLog)