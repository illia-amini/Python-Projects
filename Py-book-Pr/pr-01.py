#ex-01
#priamry-info

'''
write a code,that recive usernmae and return
welcome username
'''
Username = input('Enter ur name;')
print('Welcome',Username),

#ex-02

'''
write a code,regards str methode
'''
#1-|n & \t;
txt = 'hello\nmy name is\tali\nIm a\tstudent'
print(txt)
#2-str cut;
txt02 = 'hello my name is alireza amini'
print(txt02[:5])
print(txt02[6:16])
print(txt02[17:30])
#3-str sum;
txt03 = 'Hello my name is Alirza Amini'
txt04 = 'Im a student'
print(txt03 +' '+ txt04)
#4-str.upper() & lower();
txt05 = 'hello'
print(txt05.upper())
txt06 = 'HELLO'
print(txt06.lower())
#5-str.format()
#the best way to deifine format way write a f word behind the str 
myname = 'Alireza Amini'
age = 22
txt07 = f'Hello my name is {myname} and Im {age} years old.'
print(txt07)

#ex-03

'''
recive user info,returns as str

'''
usname = str(input('Enter ur name;'))
usage = int(input('Enter ur age;'))
uscity = str(input('Enter ur city;'))
usweight = float(input('Enter ur weight;'))
usheight = float(input('Enter ur height;'))
usemarried = bool(input('if you are single enter 1,else 0;'))
usbio = f'Hello Im {usname},\nIm {usage} yearsold,\nIm form {uscity},\nIm {usweight} kg,\nand my tall is {usheight},\nand im {usemarried} .\n'
print(usbio)