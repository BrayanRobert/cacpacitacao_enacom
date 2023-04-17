def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('/'))
    
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    if month < 1 or month > 12:
        return False
    
    if month == 2:
        if is_leap_year:
            max_day = 29
        else:
            max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
        
    if day < 1 or day > max_day:
        return False
    
    return True

date1 = '31/02/2022'
date2 = '29/02/2022'
date3 = '29/02/2024'
date4 = '30/04/2022'

print(is_valid_date(date1)) 
print(is_valid_date(date2)) 
print(is_valid_date(date3)) 
print(is_valid_date(date4)) 
