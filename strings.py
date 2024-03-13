name='anuj'
paragraph='''This is a 
mutliline 
String
paragraph.This is for testing'''
print(paragraph)

print('string indexing')
print(name[2])
print(name[-1])
print(name[-3])


print('Slicing')
s='abcde'
print(s[1:4])
print(s[1:5])
print(s[:4])
print(s[0:5:2])
print(s)
print(s[1:3])
print(s[0:5:-1])
print(s[-1:0:-1])


a='abc'
b='def'

c=a+b
print(c)
d=a*2
print(d)

e="abc"
for my_char in a:
    print(my_char*2)

s='123'
print(s.isdigit())

string='ABCDE$%'
print('s.alpha',string.isalpha())
print('s.islower',string.islower())
print('s.isupper',string.isupper())
print('s.lower',string.lower())
print('s.upper',string.upper())

x='   abc   ';
print(x.lstrip())
print(x.rstrip())