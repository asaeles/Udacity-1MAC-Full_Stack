daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year%4 != 0:
        return False
    if year%100 != 0:
        return True
    if year%400 == 0:
        return True
    return False

def daysOfWholeYears(y1, y2):
    days = 0
    while y1 < y2:
        if isLeapYear(y1):
            days += 366
        else:
            days += 365
        y1 += 1
    return days

def daysOfWholeMonths(m):
    # Takes the month number m as an input and returns
    #  the total number of days from 1st of Jan up to 
    #  given month m excluding m itself (whole months only)
    # So if takes Jan (1) as an input it will return
    #  zero becuase there are no full month before Jan
    #  in the year
    # But if it takes Feb it will surely return 31
    days = 0
    i = 0
    while i < m - 1:
        days += daysOfMonths[i]
        i += 1
    return days

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days1 = daysOfWholeMonths(m1) + d1
    days2 = daysOfWholeYears(y1, y2) + daysOfWholeMonths(m2) + d2
    days = days2 - days1
    return days

#print isLeapYear(2001)
#print daysOfWholeYears(2004,2004)
#print daysOfWholeMonths(2)
print daysBetweenDates(1981, 5, 23, 2018, 5, 19)