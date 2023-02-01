#a list with all data about fruits in shop. 0.0 is names of fruits, 0.1 is their price and 0.2 is kg available
fruktLista = [
    ["BANAN", "AVOKADO", "CLEMENTIN", "LIME", "ÄPPLE", "VINDRUVOR", "MANGO", "PÄRON", "APELSIN", "GRAPEFRUKT"],
    [34.38, 138.46, 64.95, 100.0, 34.72, 99.0, 45.45, 38.99, 27.95, 47.50],
    [12.0, 13.0, 73.0, 83.0, 55.0, 69.0, 96.0, 48.0, 43.0, 37.0]
]

#a list for customers choices: 0.0 for fruit name, 0.1 for price and 0.2 for kg
korg = [
    [],[],[]
]

fukta = ""

#a variable that takes number of customers as input to run a programm equal times
kunder = int(input("Hur många kunder: "))

def handel():
    print("Välkommen till vår butik! Här är en lista av våra frukter: ")
    for i in range(0, len(fruktLista[0])):
        if fruktLista[2][i] > 0:
            print("__________________________________________________")
            print(fruktLista[0][i] + ": " + str(round(fruktLista[1][i])) + " kr/kg. " + "Vi har", fruktLista[2][i], "kg kvar.")

    while True:
        frukta = input("\nVälj en fruk som du vill köpa (välj bara EN): ").upper()
        if not frukta in fruktLista[0]:
            print("Vi har ingen", frukta, "försök igen")
        else:
            korg[0].append(input("\nVälj en fruk som du vill köpa (välj bara EN): ").upper())
            korg[1].append(float(input("Hur mycket vill du ta? Ange värde i kg: ")))
        
            for j in range (0, len(fruktLista[0])):
                if korg[0][i] == fruktLista[0][j]:
                    korg[2].append(korg[1][i]*fruktLista[1][j])
                    fruktLista[2][j] = fruktLista[2][j] - korg[1][i]
                    print(str(korg[0][i])+ ": " + str(korg[1][i]) + "kg " + str(korg[2][i])+ "kr")
            mer = input("Vill du ha något mer? Svara ja eller nej: ")
            if mer.upper() != "JA":
                break

    print("\nKvitto:")
    sum = 0
    for i in range(len(korg[2])):
        sum += korg[2][i]
        print(str(korg[0][i]) + ", "+ str(korg[1][i]) + "kg: "+ str(korg[2][i])+"kr")
    print("Totalt: " + str(round(sum))+"kr\nNästa kund! \n")

#a main loop that runs ones for each customer
for a in range (0, kunder):
    handel()
    
