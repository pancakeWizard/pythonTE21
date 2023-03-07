def subtotal (orderAmt, salesTax=.08):
    subtotal = float(orderAmt) * (1+float(salesTax))
    return subtotal

def orderMsg():
    print("Thank you for your order(s)")
    return

firstOrderTotal = subtotal(300, .08)
secondOrderTotal = subtotal(400, 0.06)

thirdOrderAmount = input("What was the order amount? ")
thirdTax = input("Enter your sales tax rate. ")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

fourthOrderTotal = subtotal(800)

print("Your subtotal for the first order is %.2f" %firstOrderTotal)
print("Your subtotal for the second order is %.2f" %secondOrderTotal)
print("Your subtotal for the thirs order is %.2f" %thirdOrderTotal)
print("Your subtotal for the fourth order is %.2f" %fourthOrderTotal)
orderMsg()