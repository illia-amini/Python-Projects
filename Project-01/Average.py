'''
Average of nums!!!
Take the average of nums inf times,whenever user enter 0 loop break.untill that time keep counting... 
'''
#<----------code=========>
#if-you-enter-0-it-shows-error-so-do-not-think-about-to-do-it-:)
s=0#sum
q=0#quantity
while True:#it-works-untill-it-is-true
    num=int(input('Enter Average of Numbers you want,when its finished enter 0:'))
    if num==0:
        break
    s+=num#s=s+num
    q+=1#q=q+1
print("avg;",s/q)