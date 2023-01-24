animalSales = 100000
newCustomer = True
region = "North"

if animalSales >= 500000:
    print("Gold Customer")
elif animalSales >= 300000:
    print("Silver Customer")
    if region == "North":
        print("Send a snowboard")
    else: 
        print("Send a baseball bat")
elif animalSales >= 100000 and newCustomer:
    print("Bronze Customer and first-time prize winner")
elif animalSales >= 10000: 
    print("Bronze Customer")
else: 
    print("Up and Coming Customer")
print("Thank your for your business")