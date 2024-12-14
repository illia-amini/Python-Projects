#write a code, returns if usernum is + or - or 0
user_num =int(input('Enter ur number;'))
if user_num > 0:
    print('+')
elif user_num == 0:
    print("0")
elif user_num < 0:
    print('-')
else:
    print('invalid number')
#write a code, returns usernum and the opeartion which user want
user_num_01 =int(input('Enter ur  first number;'))
user_num_02 =int(input('Enter ur  second number;'))
user_op =input('operation u want;')
if user_op =='+':
    sum = f'u chose +,so:\n{user_num_01} + {user_num_02} = {user_num_01+user_num_02}'
    print(sum)
elif user_op =='-':
    sub = f'u chose -,so:\n{user_num_01} - {user_num_02} = {user_num_01-user_num_02}'
    print("sub")
elif user_op =='*':
    mul = f'u chose *,so:\n{user_num_01} * {user_num_02} = {user_num_01*user_num_02}'
    print('mul')
elif user_op =='/':
    div = f'u chose /,so:\n{user_num_01} / {user_num_02} = {user_num_01//user_num_02}'
    print(div)
elif user_op =='**':
    pow = f'u chose **,so:\n{user_num_01} ** {user_num_02} = {user_num_01**user_num_02}'
    print(pow)
else:
    print('invalid operation')
