#write a cpde to returns,leap years,also check century year
user_year =int(input('Enter ur year:'))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if(user_year % 400 == 0) and (user_year % 100 == 0):
    print('{0} is a leap year'.format(user_year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (user_year % 4 == 0) and (user_year % 100 != 0):
    print('{0} is a leap year'.format(user_year))
else:
    print('{0} is not a leap year'.format(user_year))