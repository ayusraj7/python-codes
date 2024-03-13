# print('Hello world',100) 

# name='tim'
# print('Hi . \n How are you')
# print(name.upper())
# print(name.lower())
# print(name.islower())
# print(name.isupper())
# print(bin(10))


# from math import * 
# print(pi)
# print(sqrt(100))
# print(isqrt(25))
# import random as r
# print(r.random())
# print(r.randint(0,11))

print('how are you ')
# a=int(input('input your number'))
# print('enter the number ',a)

list1=[1,2,3,4,5]
list2=['banana','apples','mango','oranges']
# list1.extend(list2)
list2.append('cherry')
list1.insert(1,12)
print(list1)
print(list2)
print(list2.count('mango'))
print(list2.index('mango'))
list2.sort()
list2.reverse()
print(list2)


# #tuples
# three_numbers=(1,2,3,1)
# print(three_numbers)
# print(len(three_numbers))
# print(type(three_numbers))
# strings=('home','land','earth')
# print(strings)

 #functions :identation is used after function declaration
# def greetings():
#     print('hello, you are welcome here ')

# greetings()

# def sum(a,b):
#     return a+b


# print('sum is ',sum(3,4))

# #functions 
# age=23
# if age>18:
#     print('you can vote ')
# else:
#     print("you can't vote")


# num=-1
# if num>0:
#     print('positive number')
# elif num==0:
#     print('zero')
# else :
#     print('negative number')


# value=input('input a value:')

# if type(value)==str:
#     print(value + 'is a string')
# elif type(value) == int:
#     print(value+'is an integer')
# elif type(value) == list:
#     print(value+'is a list')
# else:
#     print("we don't the know the data type of "+value)


#even number program 
# num=int(input('Enter the number -->'))
# if num&1:
#     print('It is a odd number ')
# else:
#     print('It is a even number ')



#while loop 
i=1
while i<6 or i==10:
    print(i)
    i=i+1


my_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(my_list[0])

 #try and except error

# try:
#     x=int(input('Input an integer '))
#     print(x)
# except:
#     print('Exception Occurs ')
# else:
#     print('everything is fine')

#reading files
print('reading files --> \n \n')
f=open('data.txt','r')
print(f.readable())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.read())

f.close()


x=open('pr.py','w')
x.write('print("hello how are you ")')


#classes and objects
class myclass:
    x=5

a=myclass()
print(a.x)


