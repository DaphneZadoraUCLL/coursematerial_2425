def parse_day(string):
    return int(string[3:5])

def parse_month(string):
    return int(string[:2])

def parse_year(string):
    return int(string[6:])

def fix_date(date):
    month = date[:2]
    day = date[3:5]
    year = date[6:]
    return f"{year}/{month}/{day}"