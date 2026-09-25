# file = open('test.txt','r')
# #print(file.read())

# ap = open('test.txt','a')
# ap.write('near the office we habe bafmati bridge \n')
# ap.write('we live in tech era\n')
# ap.close
# s=1
# lines = file.readlines()
# for line in lines:
    # print(s,line.strip())
    # s=s+1

import os
if os.path.exists('test.text'):
    os.remove('test.txt')
else:
    print('the file doesmot exist') 

#os.remove('test.txt')       
