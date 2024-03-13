
#math module

import math 
print(math.pi)
print(math.e)

#2nd way 
import math as m
print(m.cos(90))
print(m.pi)
print("Square",m.isqrt(25))

#3rd way 
from math import cos,sin
print(cos(360))
print(sin(230))

#random module 
import random 
random_number=random.randint(0,5)
print(random_number)
print('Random number ',random.random())
print('Random number ',random.random()*100);
first=['Star Plus','DD1',"Aaj Tak","CodewithHarrry"]
print('channel',random.choice(first))

#NumPy module 
import numpy as np
arr=np.array([1,2,3])
print(arr)
print(type(arr))
print(arr[0])
print(arr.shape)
print(arr.dtype)

#time module 
import time 
print(time.gmtime(0))
print(time.time())
print(time.ctime(time.time()))


#dir function 
# print(dir(time))
# print(dir(math))
# print(dir(np))
