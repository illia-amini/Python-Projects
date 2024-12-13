#write a code,returns if user nums are greater then 10 take average,otherwise so not count.(4 nums)
Number1 = int(input("Enter ur first number:"))
Number2 = int(input("Enter ur second number:"))
Number3 = int(input("Enter ur third number:"))
Number4 = int(input("Enter ur fourth number:"))
Approved_Number1 = 0
Approved_Number2 = 0
Approved_Number3 = 0
Approved_Number4 = 0
if Number1>=10:
    Approved_Number1=Number1
    print('ok,Approved')
else:
    print('less than 10')
if Number2>=10:
    Approved_Number2=Number2
    print('ok,Approved')
else:
    print('less than 10')
if Number3>=10:
    Approved_Number3=Number3
    print('ok,Approved')
else:
    print('ok,less than 10')
if Number4>=10:
    Approved_Number4=Number4
    print('ok,Approved')
else:
    print('less than 10')
print('Avereage;',(Approved_Number1+Approved_Number2+Approved_Number3+Approved_Number4)//4)
#Mind-of-king-Heart-of-warrior