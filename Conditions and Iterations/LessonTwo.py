# capitalGuess = input("What is the capital of Latvia? ")
# numberGuesses = 1

# while capitalGuess != "Riga":
#     numberGuesses+=1
#     capitalGuess = input("Guess again. ")

# print("You guessed it. Riga is the capital of Lativa. It took you" + str(numberGuesses) + "guesses.")



initialSaleGoal = 20000
multiplier = 100
offMonth = False

for monthlyGoal in range(1,13):
    if monthlyGoal == 6 and offMonth:
        print("No goal for month 6")
        continue
    monthlySaleGoal = initialSaleGoal + (monthlyGoal*multiplier)
    print("Your sales goal for moth " + str(monthlyGoal)+" is "+str(monthlySaleGoal))
    for weeklyGoal in range(1,5):
        print("Your goal for week "+ str(weeklyGoal) + " is " + str(monthlySaleGoal/4))
print("Good luck with your goals.")





# capitalGuess = input("What is the capital of Latvia? ")
# numberGuesses = 1

# while capitalGuess != "Riga":
#     numberGuesses+=1
#     if numberGuesses > 3:
#         print("You guessed incorrectly three times. Game over")
#         break
#     capitalGuess = input("Guess again. ")

# if numberGuesses <= 3:
#     print("You guessed it. Riga is the capital of Lativa. It took you" + str(numberGuesses) + "guesses.")






# annualSales = 200000
# if annualSales >= 500000:
#     print("Gold customer")
# elif annualSales >= 300000:
#     print("Silver Customer")
# elif annualSales >= 100000:
#     pass
# print("Thak you for your business")