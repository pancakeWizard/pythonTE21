import datetime

day = int(input("DD: "))
month = int(input("MM: "))
year = int(input("YYYY: "))

def yourAge(day,month,year):
    today = datetime.date.today()
    d = int(datetime.datetime.strftime(today, "%d"))
    m = int(datetime.datetime.strftime(today, "%m"))
    y = int(datetime.datetime.strftime(today, "%Y"))
    # firstDate = datetime.date.date(y, m, d)
    # secondDate = datetime.date.date(y, month, day)
    # days = int(firstDate - secondDate)
    # print(firstDate - secondDate)
    aY = y - year
    if month < m:
        aM = m - month
    else:
        aY -= 1
        minus = m - month
        aM = 12 + minus
    # k = 
    # print(k)
    return(f"You are {aY} years and {aM} month old.")

print(yourAge(day,month,year))

