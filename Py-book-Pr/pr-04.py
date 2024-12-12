#write a code,returns if user num either has two digits or one.
User_Number = int(input('Enter ur number:'))
if 10<= User_Number <100:
    print('The Enteread Number has Two digits.')
else:
    print('The Entered Number has only one digit')
#write a code,returns if user letter is capital or not.
User_letter = str(input('Enter ur letter;'))
if 'A'<=User_letter<='Z':
    print('ur letter is capital')
else:
    print('ur letter is small')
#write a code,returns if the length of two user string is eqaul or not.
#tip; func of; len(); it count the length of string
Use_String1 = str(input('Enter ur First word;'))
Use_String2 = str(input('Enter ur Second word;'))
if len(Use_String1) == len(Use_String2):
    print('Equal length')
else:
    print('Not equal length')
#Mind-of-king-heart-of-warrior