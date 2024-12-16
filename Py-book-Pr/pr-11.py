#write a code,returns if user num divide by 5 is 0
user_num = int(input('Enter ur num:'))
if user_num % 5 == 0:
    print(str(user_num),': yes')
else:
    print(str(user_num),': No')
#wreite a code to find max and min.do not use max & min func.
#1-max
user_num01 = int(input('Enter ur first num:'))
user_num02 = int(input('Enter ur second num:'))
user_num03 = int(input('Enter ur third num:'))
largest_num = user_num01
if user_num02 >= largest_num:
    largest_num = user_num02
if user_num03 >= largest_num:
    largest_num = user_num03
largest_num_str=f'the largest number is:\n{largest_num}'
print(largest_num_str)
#2-min
user_num01 = int(input('Enter ur first num:'))
user_num02 = int(input('Enter ur second num:'))
user_num03 = int(input('Enter ur third num:'))
weakest_num = user_num01
if user_num02 <= weakest_num:
    weakest_num = user_num02
if user_num03 <= weakest_num:
    weakest_num = user_num03
weakest_num_str=f'the weakest number is:\n{weakest_num}'
print(weakest_num_str)
#write a code,returns user num either is odd or even,+ or -
user_num01 = int(input('Enter ur number:'))
if user_num01 >= 0:
    if user_num01 % 2 == 0:
        print(str(user_num01),' :even and positive')
    elif user_num01 % 2 != 0 :
        print(str(user_num01),' :odd & positive')
elif user_num01 <= 0 :
    if user_num01 % 2 == 0:
        print(str(user_num01),' :even & minues')
    elif user_num01 % 2 !=0:
        print(str(user_num01),' :odd & minues')
#Matchcase-ex
day = int(input("Enter ur day:"))
match day :
    case 1:
        print('Saturday')
    case 2:
        print('Sunday')
    case 3:
        print('Monday')
    case 4:
        print('Wedsnday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case _:
        print('Error')
'''
in match case,
first u define a var,
second, u should write match varname:
instead of cas write varname,then write case input and orders
in front of case number user will give, below order u want to apply
here instead of else we have got case _ write it and below write the order u want
'''