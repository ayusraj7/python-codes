def greet():
    print('Good Morning,Anuj')

greet()

def greeting(name,dish):
    print('Good Morning',name)
    print('Please eat',dish)

greeting('Ayush','chole Bhature')

a=[1,3,6,1,9,8]
def sum_of_list(a):
    print('Calculating')
    return sum(a)

print(sum_of_list(a))

name=['ayush','darshan','divya','talki']
def greetings(names):
    for name in names:
        print('Hello',name)

greetings(name)
 