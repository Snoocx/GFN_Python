# Ist die Jahreszahl durch vier teilbar, aber nicht durch 100, ist es ein Schaltjahr. 2008 fällt unter diese Regel.
# Ist die Jahreszahl durch 100 teilbar, aber nicht durch 400, ist es kein Schaltjahr. 2100 wird kein Schaltjahr sein.
# Ist die Jahreszahl durch 400 teilbar, dann ist es ein Schaltjahr. Deshalb war das Jahr 2000 ein Schaltjahr

# Ist ein Schaltjahr, wenn das Jahr durch 4 und nicht durch 100 Teilbar
# oder durch 400 teilbar ist

def GetInputAsYear():
    return int(input("Bitte Jahr eingeben:\n"))

def CheckIfYearIsLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def main():
    year = GetInputAsYear()                               
    if CheckIfYearIsLeapYear(year):
        print(f"{year} ist ein Schaltjahr") 
    else:
        print(f"{year} ist kein Schaltjahr") 

while 1:
    main()