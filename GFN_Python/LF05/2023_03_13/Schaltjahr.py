# Ist die Jahreszahl durch vier teilbar, aber nicht durch 100, ist es ein Schaltjahr. 2008 fällt unter diese Regel.
# Ist die Jahreszahl durch 100 teilbar, aber nicht durch 400, ist es kein Schaltjahr. 2100 wird kein Schaltjahr sein.
# Ist die Jahreszahl durch 400 teilbar, dann ist es ein Schaltjahr. Deshalb war das Jahr 2000 ein Schaltjahr

def GetInputAsYear():
    return int(input("Bitte Jahr eingeben:\n"))

def CheckIfYearIsLeapYear(year):
    isLeapYear = False

    if year % 4 == 0 and year % 100 != 0:
        isLeapYear = True
    elif year % 100 == 0 and year % 400 != 0:
        isLeapYear = False
    elif year % 400 == 0:
        isLeapYear = True

    return isLeapYear

def main():
    year = GetInputAsYear()                               
    if CheckIfYearIsLeapYear(year):
        print(f"{year} ist ein Schaltjahr") 
    else:
        print(f"{year} ist kein Schaltjahr") 

main()