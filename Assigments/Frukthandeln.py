fruktLista = [
    ["BANAN", "AVOKADO", "CLEMENTIN", "LIME", "ÄPPLE", "VINDRUVOR", "MANGO", "PÄRON", "APELSIN", "GRAPEFRUKT"],
    [34.38, 138.46, 64.95, 100.0, 34.72, 99.0, 45.45, 38.99, 27.95, 47.50],
    [12.0, 13.0, 73.0, 83.0, 55.0, 69.0, 96.0, 48.0, 43.0, 37.0]
]

korg = [
    [],[],[]
]
kunder = int(input("Hur många kunder: "))
for a in range (0, kunder):
    print("Välkommen till vår butik! Här är en lista av våra frukter: ")
    for i in range(0, len(fruktLista[0])):
        print(fruktLista[0][i] + ": " + str(round(fruktLista[1][i])) + " kr/kg")

    for i in range(0, 10):
        korg[0].append(input("Välj en fruk som du vill köpa (välj bara EN): ").upper())
        korg[1].append(float(input("Hur mycket vill du ta? Ange värde i kg: ")))

        for j in range (0, len(fruktLista[0])):
            if korg[0][i] == fruktLista[0][j]:
                korg[2].append(korg[1][i]*fruktLista[1][j])
                fruktLista[2][j] = fruktLista[2][j] - korg[1][i]
            
        print(korg[0][i], ":", korg[1][i])

        mer = input("Vill du ha något mer? Svara ja eller nej: ")
        if mer.upper() != "JA":
            break

    print("Kvitto:")
    for i in range(len(korg[2])):
        print(str(korg[0][i]) + ", "+ str(korg[1][i]) + "kg: "+ str(round(korg[2][i]))+"kr"+"\n Nästa kund!")
