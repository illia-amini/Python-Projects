'''
name;
age;
city;
keep reading...
if name=0
finish
'''
try:
    list=[]
    while 1:
        name=input('name=')
        if name=='0':
         break
        #if-user-make-a-mistake-in-any-line-of-code-.-the-lower-code-wont-apply
        age=int(input('age='))
        city=input('city=')
        dict={}
        dict['name:']=age
        dict['age:']=age
        dict['city:']=city
        list.append(dict)
        for item in list:#each item in list is dict originally
            print(item)
except:
    print("Error input is not number in age")
print('end')
