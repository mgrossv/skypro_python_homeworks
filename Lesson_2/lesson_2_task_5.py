# Месяц — сезон


def month_to_season(month):
    if month in [12,1,2]:
        return "зима"
    elif month in [3,4,5]:
        return "весна"
    elif month in [6,7,8]:
        return "лето"
    elif month in [9,10,11]:
        return "осень"
    else:
        return False
    
print (month_to_season(12))
print (month_to_season(5))
print (month_to_season(8))
print (month_to_season(9))
print (month_to_season(33))