# class Person:
#     name="Harry"
#     occupation="Software Developer"
#     networth=10
#     def info(self):
#         print( f"{self.name} is a {self.occupation}")

# a=Person()
# print(a.name,a.occupation)
# print(a.info())

#constructor 
class person:
    def __init__(self,n,o):
        print("hey i am a person ")
        self.name=n
        self.occupation=o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

    def __str__(self):
        return (f"{self.name}is a {self.occupation}")
    
    #destructor 
    def __del__(self):
        print('Destructor called, Employee deleted ')

a=person("ayush","stud")
a.info()

b=person("lakshya","rani")
b.info()

#delete object property 
# del a.name

# print(a.name)

print(a.occupation)


    