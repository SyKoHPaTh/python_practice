
''' Note: 
If coding in a "thing", they typically do not allow for input().  To remedy,
need to have the code run in a separate terminal instance.
'''

import datetime 

user_year = input("What is your age in years?")
print("You entered: " + user_year)

today = datetime.date.today()

birth_year = today.year - int(user_year)

print("You were born in ", birth_year)

