def zellers_congruence(day, month, year):
    if month > 12: 
        return "month not available"
    elif day > 31:
        return "date not available"
    elif (day > 30 and (month == 4 or month == 6 or month == 9 or month == 11)) or (day > 29 and month == 2):
        return "Date not available"
    elif month < 1 or day < 1:
        return "Date and month not available"
    elif (month == 2 and day > 28 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
        return "Date not available"
    elif month < 3:
        month += 12
        year -= 1
    
    q = day
    m = month
    k = year % 100
    j = year // 100
    
    f = q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    day_of_week = f % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]

date = (4,12,2000)
day_name = zellers_congruence(*date)
print("The day of the week is:", day_name)
