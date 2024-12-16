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
