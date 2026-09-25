import pandas as pd

# ser = pd.Series()
# print(ser)

# s = pd.Series([10,20,30,40])
# print(s)
# print(s[2])

# p = pd.Series([50,60,70], index=['p','t','o'])
# print                                  
# print(p)
# print(p['p'])

# marks = [40,50,60,70]
# name = ['rakesh','barsha','ram','sita']
# s = pd.Series(marks, index = name)
# print(s)
# print(s.ndim)

# d = {'math':"50",'science': "60",'social' :"70"}
# s = pd.Series(d)
# print(s)

# s = pd.Series([10,20,30])
# print(s + 5)

s = pd.Series([10,20,30,40,50])
print(s[s > 30])
print(s[(s > 10) & (s < 50 )])
# print(s.min())
# print(s.max())
# print(s.mean())
# print(len(s))
# for i in s :
#     print(i)