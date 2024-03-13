# a=[0 ,1 ,2 ,3 ,4 ,5, 6, 7, 8, 9]
# print(a);


# a=[x for x in range(10)]
# print(a)

a=[x for x in range(100) if x%2==0]
print(a)


b=[3**i for i in range(10)]
print(b)


# lists method 
a=[1,2,3,5]
a[3]='divya'
a.append('ayush')
print(a)

print('Inserting')
a.insert(1,0.5)
print(a)

print('Sorting')
c=[4,1,3,5,1]
c.sort()
print(c)



print('Pop')
c.pop(2)
print(c)

fruits=['Banana','Apple','Kiwi']
fruits.sort()
print(fruits)


print('Reverse')
fruits.reverse()
print(fruits)

print('Indexing')
print(fruits.index('Apple'))

print('Counting')
print(fruits.count('Kiwi'))



# Lists functions
print('Prints Functions')
e=[6,2,3,9,1,6,4,5]

print(len(e))
print(max(e))
print(min(e))

s="Anuj"
print(list(s))

print(sum(e))



