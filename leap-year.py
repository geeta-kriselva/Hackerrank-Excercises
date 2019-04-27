def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
                return leap
            else:
                leap = False
                return leap
        else:
            leap = True
            return leap
    else:
        leap = False
        return leap
n = input("Enter the number: ")
year = int(n)
print(is_leap(year))
