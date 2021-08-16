class Person:

    def __init__(self,f,l): #self means current insatnce of the class
        self.fname=f
        self.lname=l
        print("Hello "+self.fname+" "+self.lname)

    def sum(self,x,y):
        self.v1=x #creating global variable
        self.v2=y
        return self.v1+self.v2

x=Person("Nikhil","Shukla")
print(x.sum(87,98))
