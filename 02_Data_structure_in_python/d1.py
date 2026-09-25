# d = {}
# print(type(d))

# d = {'name':"renuka","salary":20000, "age":19}
# print(d)
# print(len(d))
# name = d['name']
# print(name)

# for k, v in d.items():
#     print(f'key is {k}...value is : {v}')
#     if k == 'salary':
#         sal = v * 0.1
#         print('sal 10%' , sal)
# p = (d['salary']*10)/100
# print(p)

# for k in d.keys():
#     print(k)

# for v in d.values():
#     print(v)

# d['company'] = 'google'
# print(d)

# del d['company']
# print(d)

# converting touple into dic
# dt = dict([('name', 'ritu'),('id',10),('subject', 'python')])
# # print(dt)
# for k ,v in dt.items():
#     if k == 'id':
#         continue
#     print('k,.......',v)

# d3=dict(name='irenuka',age=6)
# print(d3)

# d = dict(input('enter your name:'))
# print(d)
# d = dict()
# name = input('enter your name')
# course = input('enter your course')
# fee = int (input('enter your fee'))
# d['name']=name
# d['course'] = course
# d['fee']=fee
# print(d)

def lsdict(x,y):
    if type(x) == list:
        print('list', x)
    if type(y) == dict:
        print('dict')

ls=[11,22,33]
dt= {'name':'ren', 'age':19}
lsdict(ls,dt)            
    


