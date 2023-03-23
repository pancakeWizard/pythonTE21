# import math

# pi = math.pi

# upperBound = math.ceil(44.4)
# lowerBound = math.floor(44.4)

# print(pi)
# print(upperBound)
# print(lowerBound)

# import os
# import datetime
# def clear():
#     os.system('cls' if os.name=='nt' else 'clear')

# while True:
#     todayWithTime = datetime.datetime.today()
#     todayWithoutTime = datetime.date.today()
#     print(todayWithTime)
#     print(todayWithoutTime)
#     print("The current date is", datetime.datetime.strftime(todayWithoutTime, "%Y/%m/%d"))
#     print("The current time is", datetime.datetime.strftime(todayWithTime, "%H:%M:%S"))
#     clear()

# import io
# with open("log.txt","w") as writeFile:
#     toLog = input("What do you want to write to the log?")
#     writeFile.write(toLog)


import os

dirName = input("Enter the mane of the folder you want to create. ")
os.mkdir(dirName)
print("Directory created.")