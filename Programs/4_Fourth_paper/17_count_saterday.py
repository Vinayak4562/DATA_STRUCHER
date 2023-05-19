# import datetime

# def saturdays_count(year):
    
#     date_obj = datetime.date(year, 1, 1)        # Create a datetime object for the first day of the year    
#     days_to_sat = (7 - date_obj.weekday()) % 7         # Calculate the number of days until the next Saturday    
#     second_sat = date_obj + datetime.timedelta(days_to_sat) # Add the number of days until the first Saturday to the first Saturday to get the date of the second Saturday
#     days_to_end = (datetime.date(year, 12, 31) - second_sat).days       # Calculate the number of days between the second Saturday and the end of the year
#     num_saturdays = (days_to_end // 7) + 1      # Calculate the number of Saturdays between the second Saturday and the end of the year, and add 1 to include the first Saturday
    
#     return f'Count of Saturdays in the {year} are {num_saturdays}'


# year = int(input("Enter the year: "))
# print(saturdays_count(year))


import datetime

def saturdays_count(year):
    count_saturday = 0
    date = datetime.date(year,1,1)
    while date.year == year:
        if date.weekday() == 5:
            count_saturday +=1
        date += datetime.timedelta(days=1)
    return f'Number of Saturdays in the {year} are {count_saturday}'
    

year = int(input("Enter the year: "))
print(saturdays_count(year))