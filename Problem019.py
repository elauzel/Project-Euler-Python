# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def count_sundays_falling_on_first_of_month(year_begin: int, year_end: int):
    year = 1900
    day_of_week = 1
    days_jan = 31
    days_mar = 31
    days_apr = 30
    days_may = 31
    days_jun = 30
    days_jul = 31
    days_aug = 31
    days_sep = 30
    days_oct = 31
    days_nov = 30
    days_dec = 31
    while year != year_begin:
        day_of_week = (day_of_week + days_jan + _days_feb(year) + days_mar + days_apr + days_may +
                       days_jun + days_jul + days_aug + days_sep + days_oct + days_nov + days_dec) % 7
        year += 1
    sunday_count = 0
    days_by_month = {1: days_jan, 3: days_mar, 4: days_apr, 5: days_may, 6: days_jun, 7: days_jul,
                     8: days_aug, 9: days_sep, 10: days_oct, 11: days_nov, 12: days_dec}
    while year != year_end + 1:
        for month in range(1, 13):
            if month == 2:
                days_in_month = _days_feb(year)
            else:
                days_in_month = days_by_month.get(month)
            for day_of_month in range(1, days_in_month + 1):
                if day_of_week == 0 and day_of_month == 1:
                    sunday_count += 1
                day_of_week = (day_of_week + 1) % 7
        year += 1
    return sunday_count


def _days_feb(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 29
    else:
        return 28


# def test_leap_years():
#     assert 28 == _days_feb(1899)
#     assert 28 == _days_feb(1900)
#     assert 28 == _days_feb(1901)
#     assert 28 == _days_feb(1902)
#     assert 28 == _days_feb(1903)
#     assert 29 == _days_feb(1904)
#     assert 29 == _days_feb(2000)


# def test_sunday_count():
#     assert 1 == count_sundays_falling_on_first_of_month(2016, 2016)
#     assert 2 == count_sundays_falling_on_first_of_month(2017, 2017)
#     assert 2 == count_sundays_falling_on_first_of_month(2018, 2018)
#     assert 2 == count_sundays_falling_on_first_of_month(2019, 2019)
#     assert 7 == count_sundays_falling_on_first_of_month(2016, 2019)


print("answer:", count_sundays_falling_on_first_of_month(1901, 2000))
