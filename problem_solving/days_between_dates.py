def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!
    number_of_days = 0

    while(is_date_before(year1, month1, day1, year2, month2, day2)):
        year1, month1, day1 = next_day(year1, month1, day1)
        #print("{},{},{}".format(year1,month1, day1))
        number_of_days = number_of_days+1

    print(number_of_days)
    return number_of_days


def is_date_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            return day1 < day2


def next_day(year, month, day):
    if day < days_in_month(year, month):
        return (year, month, day+1)
    elif day == days_in_month(year, month) and month != 12:
        return (year, month+1, 1)
    elif month == 12 and day == days_in_month(year, month):
        return (year+1, 1, 1)


def days_in_month(year, month):
    list_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    no_of_days = list_of_days[month - 1]  # to offset zero index in arrays
    if(is_leap_year(year)) and month == 2:
        return no_of_days + 1
    else:
        return no_of_days


def is_leap_year(year):
    non_leaps = [1800, 1900, 2100, 2200, 2300]
    if year not in non_leaps and year % 4 == 0:
        return True
    else:
        return False


def testDaysBetweenDates():

    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                            2018, 1,  1) == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                            2013, 6, 29) == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()

#print(next_day(2012, 8, 31))
