def is_valid_month(month):
    return 1 <= month <= 12


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def has_30_days(month):
    return month in (4, 6, 9, 11)


def has_31_days(month):
    return month in (1, 3, 5, 7, 8, 10, 12)


def has_28_days(month, year):
    return month == 2 and not is_leap_year(year)


def has_29_days(month, year):
    return month == 2 and is_leap_year(year)


def is_valid_date(day, month, year):
    if not is_valid_month(month):
        return False
    if has_30_days(month):
        return 1 <= day <= 30
    if has_31_days(month):
        return 1 <= day <= 31
    if has_28_days(month, year):
        return 1 <= day <= 28
    if has_29_days(month, year):
        return 1 <= day <= 29
    else:
        return False
