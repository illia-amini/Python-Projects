'''
Countdown!!!
recieve a num from user and count to 0
'''
#<----------code=========>
#1;via-while
time=int(input('Ready for countdown,so Enter ur time:'))
while time>0:
    time-=1
    print(time)
else:
    print('finsih')
#2;via-for
time=int(input('Ready for countdown,so Enter ur time:'))
for i in range(time):
    time-=1
    print(time)
#mind-of-king-,-heart-of-warriors