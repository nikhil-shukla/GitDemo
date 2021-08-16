class Person:

    def welcome(self): #inside the class alone only need to pass self
        print("Hello python")


def hello_world():
    print("Hello world")

p=Person()
p.welcome()
hello_world()

print(hello_world)
print(p.welcome)