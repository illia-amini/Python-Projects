#write a password code,
user_name = 'Ali'
pass_word = 'illia_amini2002'
print('welcome to our website;'),print('if u already have a account,enter 1'),print('if u dont have a account yet,enter 2')
enteread_num_01 = int(input("here:"))
if enteread_num_01 == 1:
    print('for ur securtiy, chose one puzzle below by its number'),print('1-Math operatin'),print('2-Geometri operation;'),print('3_Min or Max'),print('4_Second to hour or minute'),print('5-Word check')
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
    elif enteread_num_01_02 == 2:
        print('1-Area or 2-Preimeter')
        user_num01 = int(input('here:'))
        if user_num01 == 1:
            print('1-rectangle or 2-trinagle')
            user_num02 = int(input('here:'))
            if user_num02 == 1:
                print('enter ur lenght and width respectively')
                user_name03 = int(input('length:'))
                user_name04 = int(input('width:'))
                Area =f'Area of ur rectangel with {user_name03} width and,{user_name04} length is:\n{user_name04 *user_name03}'
                print(Area)
            elif user_num02 == 2:
                print('enter ur lenght and width respectively')
                user_name05 = int(input('height:'))
                user_name06 = int(input('base:'))
                Area =f'Area of ur triaangel with {user_name05} height and,{user_name06} base is:\n{(user_name05 *user_name06)//2}'
                print(Area)
        if user_num01 == 2:
            print('1-rectangle or 2-trinagle')
            user_num02 = int(input('here:'))
            if user_num02 == 1:
                print('enter ur lenght and width respectively')
                user_name03 = int(input('length:'))
                user_name04 = int(input('width:'))
                preimter =f'priemeter of ur rectangel with {user_name03} length and,{user_name04} width is:\n{(user_name04 + user_name03)*2}'
                print(preimter)
            if user_num02 == 2:
                print('enter ur lenght and width respectively')
                user_name05 = int(input('enter ur first side:'))
                user_name06 = int(input('enter ur second side:'))
                user_name07 = int(input('enter ur third side:'))
                preimter =f'priemeter of ur triaangel with {user_name05} and,{user_name06},and {user_name07} is:\n{user_name05 + user_name06 + user_name07}'
                print(preimter)
            if user_num02 != 1 and user_num02 != 2:
                print('invalid number')
    elif enteread_num_01_02 == 3:
        print('1-Min or 2-Max')
        user_num08 =int(input('here:'))
        if user_num08 == 1:
            print('Enter three numbers respectievly')
            user_num09 = int(input('First number:'))
            user_num10 = int(input('seocnd number:'))
            user_num11 = int(input('third number:'))
            min_num=min(user_num08,user_num09,user_num10)
            print('ur min number:',min_num)
        if user_num08 == 2:
            print('Enter three numbers respectievly')
            user_num12 = int(input('First number:'))
            user_num13 = int(input('seocnd number:'))
            user_num14 = int(input('third number:'))
            max_num = max(user_num12,user_num13,user_num14)
            print('ur max number:',max_num)
    elif enteread_num_01_02 == 4:
        pass
    elif enteread_num_01_02 == 5:
        user_text = input('Enter ur text:')
        print('word A will be checked.')
        if 'a' in user_text and 'A' in user_text:
            print('Yes')
        else:
            print('No')
    else:
        print('Enter a valid number!!!')
if enteread_num_01 == 2:
    pass