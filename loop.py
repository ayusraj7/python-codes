for x in range(0,10):
    print(2*x,end=" ")


a=['ayush','darshan','divya','lakshya','bobby']
for name in a:
    print(name,end=", ")

n=5
while n>=0: 
    print(n)
    n=n-1
    # or n-=1

print('Break and Continue')
for i in range(10):
    if i==6:
        break
    print(i)
print('continue')
for i in range(3,12):
    if i==80:
        continue
    print(i)