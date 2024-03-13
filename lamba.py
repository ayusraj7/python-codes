def double(x):
    return x*2

print(double(5))

z=5
# cannot acces global varibles 
x=lambda y:y*z

cube = lambda x:x*x*x

avg=lambda x,y: (x+y)/2
avg1=lambda x,y,z:(x+y+z)/3

def appl(fx,value):
    return 6+fx(value)

print(x(7))
print(cube(5))
print(avg(10,5))
print(avg1(3,5,10))
print(appl(cube,2))

