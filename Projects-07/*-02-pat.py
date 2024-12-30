'''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''
def star(num):
    count=0
    for i in range (1,star_num):
        print('*'*count)
        count+=1
        i+=1
    for i in range (1,star_num):
        print('*'*count)
        count-=1
        i+=1

star_num=int(input('Enter number of stars:'))
result=star(star_num)  
print(result)     
#mind-of-king-,-heart-of-warriors