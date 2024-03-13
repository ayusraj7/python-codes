print("Ayush")
import camelcase
c=camelcase.CamelCase()
print(c.hump("Ayush ola hu ober"))


age=24
_id=234
name2="Shivam"
# _id,_=45///this fails no other character 
# marks$=98//this fails no other character other than _,alphanumeric
# from=25//reserved keyword 

#datatypes

#numeric datatype
#float
rating=4.7
x=3.6
print('type of ',type(x))
print(type(4.7))

#int
marks=98
print(type(marks))

#complex number 
ac=3+4j
print(type(ac))

#sequence type 
name='ayush'
print(type(name))

names=['ayush','darshan','lakshya']
print(type(names))

#boolen
is_name=True
print(type(is_name))

#none
chal=None
print(type(chal))

#dictionary
#set
#mappings


#operators 
#arithmetic operators +,-,/,*,%,//,**
a=10
b=3
print(a+b)
print(a-b)
print(a/b)
print(b*0)
print(a%b)
print(a//b)
print(a**b)

#comments ''' && # this is used for comments 
'''rani biharan'''

#assignment operator +=,-=,*=,/=,%=,//=,**=
a=5
b=4
a+=5
print(a)
b-=2
print(b)
a*=2
print(a)
b/=2
print(b)

print(a)

a**=2
print(a)

b=15
print(b)
b//=3
print(b)

#relational/comparison operator  ==,!=,<,>,<=,>=
print(a==b)
print(a!=b)
print(a>b)
print(a<b)


#logical operator 
x=1
y=0
print('x and y is ',x and y)
print('x or y is ',x or y)
print('not x is  ', not x)


'''Average of three numbers '''
first_marks=97
second_marks=39
third_marks=40
avg=(first_marks + second_marks + third_marks)/3
print('average marks ',avg)


# #input and output 
# a=int(input('enter no '))
# b=int(input('enter 2nd no '))

# print('type of a ',type(a))

# print(a+b)

# last_name=input('Enter Name')
# print(last_name)

# #marks example 
# engmarks=int(input('Enter the english marks '))
# scimarks=int(input('Enter the science marks '))
# mathsMarks=int(input('Enter the math marks '))

# avg=(engmarks + scimarks+ mathsMarks)/3
# print(avg)

# avg=int(input('Enter the age '))


#conditions 
age=13
if age>18:
    print('you can vote ')
else:
    print("you can't vote")


num=5
if num>5:
    print('number is greater than 5')
elif num<5:
    print('number is less than 5')
else:
    print('number is equal to 5')


a=range(10)
print(a)
for i in a:
    print(i)

b=list(range(5,10))
print(b)

c=list(range(9,20,2))
print(c)

string='ayush kumar rajput '
for i in string:
    print(i)

for i in b:
    print(i)

n=6
while n>=0:
    print(n)
    n=n-1

print('break and continue ')

for i in range(1,25):
    if i==13:
        break
    print(i)


print('continue')
for i in range(0,5):
    if i==2:
        continue
    print(i)


name='Ayush Kumar'
print(name[3])
print(name[3:9])
print(name[:5])
print(name[0:5:2])
print(name[-1])
print(name[-1:5:-1])


#python strings 
string='  ABCDE%#  '
print(string.isalpha())
print(string.isdigit())
print(string.isupper())
print(string.islower())
print(string.lower())
print(string.upper())
print(string.rstrip())
print(string.lstrip())

#lists 
name='Anuj'
name=234

my_list=[1,2,3,'anuj']
print(my_list)
print(my_list[2])
print(my_list[-1])
my_list[1]='Ayush'
print(my_list)
'''deleting in list '''
del my_list[0]
print(my_list)


#list methods and operations 
no=[3,5,1,9,10]
print('maximum length ',len(no))
print('minimum length',max(no))
print('minimum',min(no))
print('sum',sum(no))
print('append',no.append(6))
print('insert',no.insert(2,34))
print(no)
no.sort()
print('sorted no ',no)
no.reverse()
print('reverse',no)
no.pop()
print(no)
no.remove(10)
print(no)
print(no.count(3))
print('index of 9 is',no.index(9))
no.clear()
print(no)

# s='anuj'
# s[0]=c
# print(s[0])

my_tuple=(1,3,5)
print(my_tuple)
#my_tuple[1]=4 tupples are immutable 

dict={1:'apple',2:'ball'}
print(dict)
for i in dict:
    print(i,dict[i])

dict[1]='bananana'
print(dict)
print('type',type(dict))
c=dict.copy()
print('c',c)

print('value of key 1',dict.get(1))
print(dict.values())
dict.pop(2)
print(dict)
dict.clear()
print(dict.keys())
print(dict)

#set :only contains unique elements 
a={1,2,4,6,4,6,2}
print(a)

#modules
import math
print(math.pi)
print('square root ',math.isqrt(25))
print(math.cos(90))
print(math.e)

#from statement 
import math as m 
print(m.pi)

from math import cos,sin
print(cos(0))


#functions 
def greeting():
    print('Lakhsya chutiya')

greeting()

def greeting(name,dish):
    print('rani was not able to make ',dish)
    print('so who are you ',name)


greeting('ayush','paneer ka pakora')


def sumoflist(list):
    print('calculating')
    return sum(list)

print(sumoflist(a))

#built in modules 
import math 
print(math.floor(0.25))
print(math.pi)

#random 
import random 
print(random.random())
print('interger ranodm ',random.randint(1,6))


import numpy as np
arr=np.array([1,2,3])
print(arr)
print(type(arr))
print(arr[0])


import time
print(time.time())


#lamba function 
z=5
x=lambda y:y*z
print(x(5))
sum=lambda x,y:x+y
print('sum',sum(3,5))
cube=lambda x:x*x*x
print('cube',cube(5))

avg=lambda x,y:(x+y)/2 
print('average',avg(14,16))


class person:
    name="harry"
    occupation="Software developer "
    networth=10


a=person()
print(a.name)
print(a.name,a.occupation)

class person:
    name="Harry"
    occupation="Software Developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
a.name="shubham"
a.occupation="Accountant"
a.info()

class person:
    def __init__(self,n,o):
        print("hey i am person")
        self.name=n
        self.occupation=o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

    def __del__(self):
        print("Destructor called, Employee deleted ")


a=person('Ayush','Software mechanic')
a.info()


print(dir(math))







    




