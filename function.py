def greet():
     print("hello")
     return greet()
# print(great()for i in range(10)) 
g_var =10
def scope():
    l_var=5
    print(g_var,l_var) 
def subm(a=2,b=4):
    print(a-b)
    return a+b
#libararies of python
import math
x=19.8
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
x=2
print(math.exp(x))
print(math.log10(x))
print(math.sin(x))
print(math.pi)

#import random function
import random
# random.seed(40)
print(random.random())
print(random.randint(1,11))
print(random.choice([2,4,5,6]))
print(random.sample([4,6,5,],2))
#print(random.uniform([1.0,3.0]))

#dateline implementation
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime(2025,11,28,10,30,0))
# print(datetime.datetime.now().strftime("%m/%d/%y  %H:%M:%S"))
# date_1 = datetime.datetime(2025,3,5,8,0)
# date_2 = datetime.datetime.now()
# print(date_2-date_1)

# # collection 
from collections import Counter , defaultdict
lst=[1,2,3,4,5,6,6,]
print(Counter(lst))
print('-'*20)

d= defaultdict(int)
d['a']+=2
print(d)

# d= orderedDict()
# d['one']=1
# print(d)