# firstName = "Kirill"
# lastName = "Yasny"
# print(lastName + ", " + firstName)

# price = 3.95
# widgets = 5
# print("The price of the widgets is:", price)
# print("We have", widgets, "in stock.")
# ~~~~~~~~~~~~~~^~~~~~~~~^~~~~~~~~~~~~~

# type casting
# print("We have " + str(widgets) + " in stock")
# print(price*widgets)
# print(int(price), float(widgets))

# north = 200
# south = 300
# northwins = north > south
# southwins = south > north
# print("Northwins = ",northwins, "\nSouthwins = ", southwins)


#-----DATA STRUCTURS-----
region = ["North", "South", "East", "West"]
sales = [30000,20000,40000,35000]
employees = ["Alice", "Vera", "Flo", "Mel"]
locations = []

for employee in employees:
    print(employee)

employees.append("Belle")
employees.remove("Flo")
employees.sort()

print("New list:")

for employee in employees:
    print(employee)