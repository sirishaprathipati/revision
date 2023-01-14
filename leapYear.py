ch=int(input('Enter a Year:'))
def leapYear(yr):
    leapyear=True

    if yr%4==0:
        return leapyear
    else:
        return False

leapYear(ch)