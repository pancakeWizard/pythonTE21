from operator import itemgetter
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    total = 0

#variabel för som gör det möjlig för kunder att köpa so mycket frukter så mycket gånger som de vill
i = 0

#a function that clears lists with information about client
def newClient():
    korg[0] = []
    korg[1] = []
    korg[2] = []
    total = 0
    i = 0

#a list with all the information about fruits, how much is available and price/kg.
fruktLista = [
    ["BANAN", "AVOKADO", "CLEMENTIN", "LIME", "ÄPPLE", "VINDRUVOR", "MANGO", "PÄRON", "APELSIN", "GRAPEFRUKT"],
    [34.38, 138.46, 64.95, 100.0, 34.72, 99.0, 45.45, 38.99, 27.95, 47.50],
    [12.0, 13.0, 73.0, 83.0, 55.0, 69.0, 96.0, 48.0, 43.0, 37.0]
]

#a shopping-list to write information about what, how much and price for the customer
korg = [
    [],[],[]
]

#a variable that takes the number of customers as input to run the main part of the program equal number times.
kunder = int(input("Hur många kunder: "))

#variabel to calculate total price
total = 0

#a function that prints the list of products. I use \t which works as a tab-button so the list seems better.
def varor():
    for i in range(len(fruktLista[0])):
        print(fruktLista[0][i] + ", " +  "  \t i lager: "+ str(fruktLista[2][i]) + "kg    \t" + str(int(fruktLista[1][i])) + " kr/kg")
       
#main loop that runs for every customer.
for kund in range(kunder):
    newClient()
    #welcome-message and price list for customers.
    clear()
    print("Välkommen till vår butik! Här är en lista av våra frukter: ")
    varor()
    #This loop needs to output product and price correctly. It's a while loop because we want to give a possibility to buy as many times a client want.
    while i >= 0:
        #validation of fruit input: is there this fruit in the store? If not - try again
        while True:
             #variabel to input fruit from user and then validate it
            frukt = input("Välj EN frukt: ").upper()
            if frukt in fruktLista[0]:
            #if fruits is available, asking how much user want to take and add the elements to the "shopping cart"-list
                korg[0].append(frukt)
                break
            else:
                clear()
                print("Vi har ingen", frukt, "försök igen. Här är en lista av våra frukter:")
                varor()
        #to calculate price for the product we need a loop where we comparing data from shopping list and available fruits list
        for el in range(len(fruktLista[0])):
            if korg[0][i] == fruktLista[0][el]:
                #We need to know how much of the fruit a client wants to have. We use while loop that will work until we go out of it with help of break
                while True:
                    massa = float(input("Hur mycket kg vill du ta: "))
                    #Here we are looking for our fruit and how much is available.
                    #If we have the number of kg that client want to buy - go out of loop and do next code
                    #If the client wants more than we have - print a message with information about max number of kg.
                    if massa <= fruktLista[2][el]:
                        korg[2].append(massa)
                        break
                    else: print("Vi har bara", fruktLista[2][el])
                #adding a price of product clculated by formula: price/kg*number of kg
                korg[1].append(float(fruktLista[1][el]*korg[2][i]))
                #subtraction bought kg of the product
                fruktLista[2][el] -= korg[2][i]
                #prints what, how much and for which price the customer bought
                print(korg[0][i], korg[2][i], "kg   \t", korg[1][i],"kr")
        #asking if the customer wants to buy something more. If not - we go out of loop, print check and start with the next customer.
        if input("Vill du ta något mer? (Ja eller Nej?)").upper() != "JA":
            break
        i += 1
    #simple output of check
    print("\nKvitto:")
    for kel in range(len(korg[0])):
        print(korg[0][kel] + ", " +  "  \t "+ str(korg[2][kel]) + "kg    \t" + str(round(korg[1][kel])) + " kr")
        total += korg[1][kel]
    print("Totalt:",total,"kr")
    if kund < kunder-1:
        input("Nästa kund! (Tryck på någon knapp för att fortsätta)")