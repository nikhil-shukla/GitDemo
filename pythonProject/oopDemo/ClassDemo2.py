class Person:

    def welcome(self): #inside the class alone only need to pass self
        print("Hello python")

    def hello_world(self):
        print("Hello world")

    def sum(self,num1,num2):
        print(num1+num2)

p=Person()
#Person.welcome(p) #internally p is transferred to self in class function which is nothing but methods
p.welcome()
p.sum(5,12.5)

#setting varible of class

q=Person()
q.name="Nikhil"
q.phone=7415908746
q.country="India"
q.city="Blr"

r=Person()
r.name="Chhaya"
r.phone=8910499110
r.country="canada"

print(q.name)
print(q.city)
print(r.country)

