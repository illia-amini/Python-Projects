#write a code,returns the min among 4 user number.
Number1 = int(input("Enter ur first number:"))
Number2 = int(input("Enter ur second number:"))
Number3 = int(input("Enter ur third number:"))
Number4 = int(input("Enter ur fourth number:"))
Minn = Number1
if Number2<Minn:
    print('the second number is min:',Number2)
if Number3<Minn:
    print('the third number is min:',Number3)
if Number4<Minn:
    print('the fourth number is min:',Number4)
else:
    print('the first number is min:',Number1)
#================= Another-methode==================
Number1 = int(input("Enter ur first number:"))
Number2 = int(input("Enter ur second number:"))
Number3 = int(input("Enter ur third number:"))
Number4 = int(input("Enter ur fourth number:"))
print('ur min num is;',min(Number1,Number2,Number3,Number4))
#write a code,returns the max among 4 user number.
User_Number1 = int(input("Enter ur first number:"))
User_Number2 = int(input("Enter ur second number:"))
User_Number3 = int(input("Enter ur third number:"))
User_Number4 = int(input("Enter ur fourth number:"))
Maxx = User_Number1
if User_Number2>Maxx:
    print('the second number is max:',User_Number2)
if User_Number3>Maxx:
    print('the third number is max:',User_Number3)
if User_Number4>Maxx:
    print('the fourth number is max:',User_Number4)
else:
    print('the first number is max:',User_Number1)
#================= Another-methode==================
User_Number1 = int(input("Enter ur first number:"))
User_Number2 = int(input("Enter ur second number:"))
User_Number3 = int(input("Enter ur third number:"))
User_Number4 = int(input("Enter ur fourth number:"))
print('ur max num is;',max(User_Number1,User_Number2,User_Number3,User_Number4))
#Mind-of-king-Heart-of-warrior