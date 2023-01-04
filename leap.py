#leap (4 % == 0 and 100 % != 0) or (400 % == 0)

year = False
def leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    elif(year % 1 == 0):
        return False


    if year == True:
        print("Leap year")
    elif year == False:
        print("not Leap year")


leap = int(input("Enter leap year! "))

print(leap_year(leap))

