import re

# st = '''Rohit is 22 years old and Dipika is 11 years old Chandan is 43 yrs old, Gautam is 5 yrs old, Ram is 111 yrs old'''

# ages = re.findall(r'\d{1,3}', st)
# print(ages)

# names = re.findall(r'[A-Z][a-z]*',st)
# print(names)

# y = re.findall(r'[A-Z]',st)

# print(y)

# nameAgeDict = {}
# x=0
# for name in names:
#     #print(name)
#     nameAgeDict[name]= ages[x]
#     x=x+1

# print(nameAgeDict)  

#mobile no val
# mob = input('enter your mobilr no:')
# reg = re.fullmatch('[7-9][0-9]{9}',mob)
# if reg != None:
#     print('valid mob no:', mob)
# else:
#     print('invalid mob no format')  


# email validation
# regx = r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9.]+$'
# email = 'renuka_scd.9+*@gmail.com'
# print(re.match(regx,email))

# if re.match(regx,email):
#     print('valid email')
# else:
#     print('invalid email')    

def email(x):
    regx = r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9.]+$'
    if re.match(regx,email):
    #    print('valid email')
       return email

    else:
    #    print('invalid email')
       return 'invalid email:'+email  
       

x = email('renuka123+-@gmail.com') 
em = email(x)
print(em)        


