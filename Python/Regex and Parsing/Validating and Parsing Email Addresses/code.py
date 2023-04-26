import email.utils
import re

n = int(input())

for i in range(n):
    name, email_address = email.utils.parseaddr(input())
    
    # check if email address is valid
    if re.match(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_address):
        print("{} <{}>".format(name, email_address))
