'''
name;
age;
city;
keep reading...
if name=0
finish
'''
list=[]
while 1:
    name=input('name=')
    if name=='0':
        break
    age=int(input('age='))
    city=input('city=')
    dict={}
    dict['name:']=age
    dict['age:']=age
    dict['city:']=city
    list.append(dict)
for item in list:#each item in list is dict originally
    print(item)