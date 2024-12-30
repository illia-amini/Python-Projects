user_num=int(input('Enter ur num:'))
count=0
for i in range(1,user_num+1):#for *
    for j in  range (1,(user_num-i)+1):#for sapces
        print(end='  ')#make 2 spaces here
    while count!=(2*i-1):
        print("* ", end="")
        count += 1
   
    count = 0
    print()
 #mind-of-king-,-heart-of-warriors