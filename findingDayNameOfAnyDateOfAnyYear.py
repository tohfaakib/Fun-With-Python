def getDayName(date, month, year):
    months = {'jan': 0, 'feb': 3, 'mar': 3, 'apr': 6, 'may': 1, 'jun': 4, 'jul': 6, 'aug': 2,
              'sep': 5, 'oct': 0, 'nov': 3, 'dec': 5}

    days = {0: 'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday'}

    sum = date + months[month] + (year - 1900) + ((year - 1900) // 4)

    return days[sum % 7]


if __name__ == "__main__":
    date, month, year = input("Enter a date of  month of a year(ex: 22 apr 1996):\n").split(" ")
    date, month, year = int(date), str(month).lower(), int(year)
    print(getDayName(date, month, year).capitalize())

