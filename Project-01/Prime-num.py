'''
Prime Number!!!
recive a num from user and shows all smaller prime num then recivied num
'''
#<----------code=========>
#Nesting-loop
num=int(input('Prime Numbers you want:'))
for j in range(2,num):
    for i in range(2,j):
        if j%i==0:
            break
    else:
       print(j)
#mind-of-king-,-heart-of-warriors