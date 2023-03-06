region = "West"
annualSales = 500000
firstName = "Tony"
if annualSales >= 500000:
    print("Gold customer")
elif annualSales >= 30000:
    print("Silver customer")
elif annualSales >= 10000:
    print("Bronze customer")
print("Thank you for your business")
print(f"Your sales representative is {firstName}" \
      f"you are in the {region} region, and you had "\
        f"{annualSales} in last year. Thanks!")
