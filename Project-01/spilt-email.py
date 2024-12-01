
'''
seperate the email part
recive a email and seperate it like ex below;
email: info@amirhn.ir
info
amirhn.ir
'''
email=input('Enter ur email address:')
char=email.find('@')
username=email[:char]
domain=email[char+1:]
print(username)
print(domain)