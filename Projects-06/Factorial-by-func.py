'''
wrie a code,
calclute factorail,
by reqercively func.
'''
def factorail(x):
    if x==0:
        return 1
    else:
        return   x * factorail(x-1)
num=int(input('plz enter a positive number:'))
result= factorail(num)
print(f'the factorial of {num} is:{result}')
