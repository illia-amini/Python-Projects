#ex-02
#Operations
#01-Mathematic Operations;
# +,/,-,*,//,**,%
#ex
num1 = int(input('enter num1;'))
num2 = int(input('Enter ur num2;'))
print('sum;',num1 + num2)
print('mince;',num1 - num2)
print('divison;',num1 / num2)
print('time;',num1 * num2)
print('power;',num1 ** num2)
print('divioin(int);',num1 // num2)
print('%;',num1%num2)
#ex02
num3 = int(input('enter num1;'))
num4 = int(input('Enter ur num2;'))
num3+=num4#also you can write -=,/=,%=,//=
print(num3)
#02-Comprasion Operation;
# ==,!=,<,>,>=,<=,and,or
#ex
num5 = int(input('enter ur num1;'))
num6 = int(input('enter ur num2;'))
if num5 == num6:
    print('==')
elif num5 != num6:
    print('!=')
    if num5 < num6:
        print('<')
    elif num5 > num6:
        print('>') 
#ex02
age =int(input('Enter ur age;'))
print(age < 20 and age > 10)
#ex03
age2 = int(input('Enter ur age;'))
print(age == 20 or age == 18)

