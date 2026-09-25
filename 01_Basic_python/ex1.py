# x = 10
# y = 0
# z = x/y
# print(z)

# x = 10
# y = 10
# try:
#     z = x/y
#     print(z)
# except Exception as e:
#     print(e) 
# else:
#     print('runs when no error in try block') 
# finally:
#     print('always runs')        


# print('last line')

def num(a, b):
    try:
        d = a/b
        print(d)
    except Exception as e:
        print(e)

num(10,5)
num(10,0)

print('last line')


