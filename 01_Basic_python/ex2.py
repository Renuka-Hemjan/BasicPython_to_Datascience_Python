# 12

# def age(age):
#     age = 12
#     if age <= 18:
#         print('lesser age')
#         raise ValueError('Invalid age value')
#     else:
#         print('valid age for voting')
# except Exception as e:
#     print(e)
    
#custom Exception

class BalanceException(Exception):
    pass
def chk_balance():
    earn = 10000
    exp = 9000
    bal = earn - exp 
    if bal < 2000:
        raise BalanceException('not sufficient amount left')
    else:
        print('sufficient amount', bal)
try:
    chk_balance()
except BalanceException as b:
    print (b) 

# num = 'python'
# num = "200"
# try:
#     print(float(num))
# except ValueError:
#     print('Invalid numerical value')
