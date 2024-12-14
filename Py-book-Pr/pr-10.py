#write a password code,
user_name = 'Ali'
pass_word = 'illia_amini2002'
print('welcome to our website;'),print('if u already have a account,enter 1'),print('if u dont have a account yet,enter 2')
enteread_num_01 = int(input("here:"))
if enteread_num_01 == 1:
    print('for ur securtiy, chose one puzzle below by its number'),print('1-Math operatin'),print('2-Geometri operation;'),print('3_Min or Max'),print('4_Second to hour or minute'),print('5-Capitall or small')
    enteread_num_01_02 =int(input('here;'))
    if enteread_num_01_02 == 1:
        user_num_01 =int(input('Enter ur  first number;'))
        user_num_02 =int(input('Enter ur  second number;'))
        user_op =input('operation u want;')
        if user_op =='+':
            sum = f'u chose +,so:\n{user_num_01} + {user_num_02} = {user_num_01+user_num_02}'
            print(sum),print('welcome')
        elif user_op =='-':
            sub = f'u chose -,so:\n{user_num_01} - {user_num_02} = {user_num_01-user_num_02}'
            print(sub),print('welcome')
        elif user_op =='*':
            mul = f'u chose *,so:\n{user_num_01} * {user_num_02} = {user_num_01*user_num_02}'
            print(mul),print('welcome')
        elif user_op =='/':
            div = f'u chose /,so:\n{user_num_01} / {user_num_02} = {user_num_01//user_num_02}'
            print(div),print('welcome')
        elif user_op =='**':
            pow = f'u chose **,so:\n{user_num_01} ** {user_num_02} = {user_num_01**user_num_02}'
            print(pow),print('welcome')
    elif enteread_num_01_02 == 1:
        pass
    elif enteread_num_01_02 == 2:
        pass
    elif enteread_num_01_02 == 3:
        pass
    elif enteread_num_01_02 == 4:
        pass
    elif enteread_num_01_02 == 5:
        pass
    else:
        print('Enter a valid number!!!')
if enteread_num_01 == 2:
    pass