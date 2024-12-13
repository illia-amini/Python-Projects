'''
choose;1-add or 2-remove
1
you want to add:)
Enter ur name;
ali
['ali']
choose;1-add or 2-remove
2
you want to remove:(
Enter ur name;
ali
['']
3
Are you ...!!!!,choose between either 1 or 2 broo
'''
studentnames=[]
while 1:# while 1 means while true,moreover,while 0 means while false
    select=int(input('Choose 1.add or 2.delete\n'))#\n,will creat a new line
    if select==1:
        print("you want to add:)")
        name=input('Enter ur name:')
        studentnames.append(name)
        print(studentnames)
    elif select==2:
        print('you want to remove:(')
        name=input('Enter ur name:')
        studentnames.remove(name)
        print(studentnames)
    elif select !=1 and 2:
        print('Are you ...!!!!,choose between either 1 or 2 broo')
#mind-of-king-,-hear-of-warrior
