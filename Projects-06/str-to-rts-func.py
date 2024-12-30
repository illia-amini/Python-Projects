'''
write a code,
recive a str as parameter,
and reverse it.
ex; amir => rima
'''
def reverse(x):
    result = ''
    for i in x:
        result=i+result
    return result
print(reverse('amir'))